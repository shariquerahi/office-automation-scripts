package main

import (
	"context"

	"github.com/pkg/errors"
	"go.uber.org/zap"

	actorPb "github.com/epifi/gamma/api/actor"
	bankCustPb "github.com/epifi/gamma/api/bankcust"
	ffPb "github.com/epifi/gamma/api/firefly"
	ffEnumsPb "github.com/epifi/gamma/api/firefly/enums"
	"github.com/epifi/gamma/api/types"
	userPb "github.com/epifi/gamma/api/user"
	vgPb "github.com/epifi/gamma/api/vendorgateway"
	ccVgPb "github.com/epifi/gamma/api/vendorgateway/lending/creditcard"
	"github.com/epifi/gamma/pkg/cfg"
	"github.com/epifi/gamma/pkg/epifigrpc"
	"github.com/epifi/gamma/pkg/logger"
)

func GetFederalCustomerDetailsForActorId(ctx context.Context, actorId string) (*userPb.GetCustomerDetailsResponse, error) {
	userConn := epifigrpc.NewConnByService(cfg.USER_SERVICE)
	userClient := userPb.NewUsersClient(userConn)

	actorConn := epifigrpc.NewConnByService(cfg.ACTOR_SERVICE)
	actorClient := actorPb.NewActorClient(actorConn)

	defer func() {
		epifigrpc.CloseConn(userConn)
		epifigrpc.CloseConn(actorConn)
	}()

	actorDetails, err := actorClient.GetActorById(ctx, &actorPb.GetActorByIdRequest{Id: actorId})
	if te := epifigrpc.RPCError(actorDetails, err); te != nil {
		return nil, errors.Wrap(te, "error in fetching actor details for the user")
	}

	customerDetails, err := userClient.GetCustomerDetails(ctx, &userPb.GetCustomerDetailsRequest{
		Vendor:     vgPb.Vendor_FEDERAL_BANK,
		UserId:     actorDetails.GetActor().GetEntityId(),
		ActorId:    actorId,
		Provenance: userPb.Provenance_APP,
	})
	if te := epifigrpc.RPCError(customerDetails, err); te != nil {
		return nil, errors.Wrap(te, "error in fetching user details for the user")
	}

	return customerDetails, nil
}

func ReqPhysicalCard(ctx context.Context, actorIds []string) error {
	bankCustConn := epifigrpc.NewConnByService(cfg.BANK_CUSTOMER_SERVICE)
	bankCustClient := bankCustPb.NewBankCustomerServiceClient(bankCustConn)

	userConn := epifigrpc.NewConnByService(cfg.USER_SERVICE)
	userClient := userPb.NewUsersClient(userConn)

	ccVgConn := epifigrpc.NewConnByService(cfg.VENDOR_GATEWAY_SERVICE)
	ccVgClient := ccVgPb.NewCreditCardClient(ccVgConn)

	ffConn := epifigrpc.NewConnByService(cfg.FIREFLY_SERVICE)
	ffClient := ffPb.NewFireflyClient(ffConn)

	defer func() {
		epifigrpc.CloseConn(ccVgConn)
		epifigrpc.CloseConn(userConn)
		epifigrpc.CloseConn(bankCustConn)
		epifigrpc.CloseConn(ffConn)
	}()

	for _, actorId := range actorIds {
		ccRes, rpcErr := ffClient.GetCreditCard(ctx, &ffPb.GetCreditCardRequest{
			GetBy:            &ffPb.GetCreditCardRequest_ActorId{ActorId: actorId},
			SelectFieldMasks: nil,
		})

		if err := epifigrpc.RPCError(ccRes, rpcErr); err != nil {
			return errors.Wrap(err, "error fetching card")
		}

		crRes, rpcErr := ffClient.GetCardRequestByActorIdAndWorkflow(ctx, &ffPb.GetCardRequestByActorIdAndWorkflowRequest{
			ActorId:             actorId,
			CardRequestWorkFlow: ffEnumsPb.CardRequestWorkFlow_CARD_REQUEST_WORKFLOW_TYPE_CARD_ONBOARDING,
		})
		if err := epifigrpc.RPCError(crRes, rpcErr); err != nil {
			return errors.Wrap(err, "error fetching card req")
		}

		bcRes, rpcErr := bankCustClient.GetBankCustomer(ctx, &bankCustPb.GetBankCustomerRequest{
			Vendor:     vgPb.Vendor_FEDERAL_BANK,
			Identifier: &bankCustPb.GetBankCustomerRequest_ActorId{ActorId: actorId},
		})
		if err := epifigrpc.RPCError(bcRes, rpcErr); err != nil {
			return errors.Wrap(err, "error fetching bank customer")
		}

		userRes, rpcErr := userClient.GetAllAddresses(ctx, &userPb.GetAllAddressesRequest{
			UserId: bcRes.GetBankCustomer().GetUserId(),
		})
		if err := epifigrpc.RPCError(userRes, rpcErr); err != nil {
			return errors.Wrap(err, "error fetching addresses")
		}

		addressType := crRes.GetCardRequest().GetRequestDetails().GetAddressType()
		addresses := userRes.GetAddresses()
		address, ok := addresses[addressType.String()]
		if !ok || len(address.GetAddresses()) == 0 {
			return errors.New("no address for the type found for the customer")
		}

		addressList := make([]*types.AddressWithType, 0)
		addressList = append(addressList, &types.AddressWithType{
			Type:    types.AddressType_SHIPPING,
			Address: address.GetAddresses()[0],
		})
		// Request physical card for actors
		logger.Info(ctx, "initiating request physical card")
		vgRes, rpcErr := ccVgClient.RequestPhysicalCard(ctx, &ccVgPb.RequestPhysicalCardRequest{
			Header:       &vgPb.RequestHeader{Vendor: vgPb.Vendor_M2P},
			EntityId:     bcRes.GetBankCustomer().GetVendorCustomerId(),
			KitNo:        ccRes.GetCreditCard().GetVendorIdentifier(),
			AddressDto:   &ccVgPb.AddressDto{Address: addressList},
			CardMaterial: ccVgPb.CardMaterial_CARD_MATERIAL_PLASTIC,
		})
		if err := epifigrpc.RPCError(vgRes, rpcErr); err != nil {
			if !vgRes.GetStatus().IsAlreadyExists() {
				logger.Error(ctx, "error in req physical card", zap.Error(err))
				return errors.Wrap(err, "error requesting physical card vg")
			}
		}
		logger.Info(ctx, "vg res", zap.String(logger.ACTOR_ID_V2, vgRes.String()))
	}
	return nil
}

func IssuePhysicalCard(ctx context.Context, actorIds []string) error {
	ffConn := epifigrpc.NewConnByService(cfg.FIREFLY_SERVICE)
	ffClient := ffPb.NewFireflyClient(ffConn)

	defer func() {
		epifigrpc.CloseConn(ffConn)
	}()

	for _, actorId := range actorIds {
		ccRes, rpcErr := ffClient.GetCreditCard(ctx, &ffPb.GetCreditCardRequest{
			GetBy:            &ffPb.GetCreditCardRequest_ActorId{ActorId: actorId},
			SelectFieldMasks: nil,
		})

		if err := epifigrpc.RPCError(ccRes, rpcErr); err != nil {
			return errors.Wrap(err, "error fetching card")
		}

		ffRes, rpcErr := ffClient.InitiateCardReq(ctx, &ffPb.InitiateCardReqRequest{
			CardId:              ccRes.GetCreditCard().GetId(),
			CardRequestWorkFlow: ffEnumsPb.CardRequestWorkFlow_CARD_REQUEST_WORKFLOW_TYPE_ISSUE_PHYSICAL_CARD,
			Provenance:          ffEnumsPb.Provenance_PROVENANCE_APP,
		})
		if err := epifigrpc.RPCError(ffRes, rpcErr); err != nil {
			return errors.Wrap(err, "error issuing physical card")
		}
	}
	return nil
}
