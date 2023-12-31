// nolint:dupl,unused,deadcode,gosec,funlen
package main

import (
	"context"
	"flag"
	"fmt"
	"os"
	"time"

	"go.uber.org/zap"
	"google.golang.org/protobuf/types/known/timestamppb"

	cardProvPb "github.com/epifi/gamma/api/card/provisioning"
	"github.com/epifi/gamma/api/investment/mutualfund/order/filegenerator"
	typesPb "github.com/epifi/gamma/api/types"
	"github.com/epifi/gamma/pkg/cfg"
	"github.com/epifi/gamma/pkg/epifigrpc"
	"github.com/epifi/gamma/pkg/logger"
)

var (
	date = flag.String("date", "", "date in  YYYYMMDD format")
)

func main() {
	flag.Parse()
	env, err := cfg.GetEnvironment()
	if err != nil {
		panic(err)
	}

	logger.Init(env)
	defer func() {
		_ = logger.Log.Sync()
	}()
	ctx := context.Background()

	// Get connection to Card Provisioning service
	carProvConn := epifigrpc.NewConnByService(cfg.CARD_SERVICE)
	defer epifigrpc.CloseConn(carProvConn)
	cardProvClient := cardProvPb.NewCardProvisioningClient(carProvConn)

	req := &cardProvPb.InitiatePhysicalCardDispatchRequest{
		CardId:      "f34687e1-e0e1-44be-a7bf-4be25b37ee0c",
		ActorId:     "AC5hRrozSHT1Our386xyU3qw230619==",
		Amount:      nil,
		AddressType: typesPb.AddressType_SHIPPING,
	}
	initiateDispatchRequestRes, err := cardProvClient.InitiatePhysicalCardDispatch(ctx, req)

	switch {
	case err != nil:
		logger.Error(ctx, "error in InitiatePhysicalCardDispatch", zap.String(logger.CARD_ID, req.GetCardId()),
			zap.Error(err), zap.String(logger.ACTOR_ID_V2, req.GetActorId()))
	case initiateDispatchRequestRes.GetStatus().GetCode() == uint32(cardProvPb.InitiatePhysicalCardDispatchResponse_INSUFFICIENT_FUNDS):
		logger.Error(ctx, "precondition failed to initiate card dispatch", zap.String(logger.CARD_ID, req.GetCardId()),
			zap.Error(err), zap.String(logger.ACTOR_ID_V2, req.GetActorId()))
	case !initiateDispatchRequestRes.GetStatus().IsSuccess():
		logger.Error(ctx, "non success status for initiating card dispatch request", zap.String(logger.ACTOR_ID_V2, req.GetActorId()),
			zap.String(logger.STATUS_CODE, initiateDispatchRequestRes.GetStatus().String()))
	default:
		logger.Debug(ctx, "initiated card dispatch successfully", zap.String(logger.CARD_ID, req.GetCardId()),
			zap.String(logger.ACTOR_ID_V2, req.GetActorId()))
	}
}

func downloadCreditMisReport() error {
	env, err := cfg.GetEnvironment()
	if err != nil {
		panic(err)
	}

	logger.Init(env)
	defer func() {
		_ = logger.Log.Sync()
	}()

	if date == nil || *date == "" {
		logger.ErrorNoCtx("date should not be empty")
		return fmt.Errorf("date should not be empty")
	}

	dateInTime, err := time.Parse("20060102", *date)
	if err != nil {
		logger.Fatal(fmt.Sprintf("failed to convert date: %s to time", dateInTime), zap.Error(err))
		return fmt.Errorf("failed to convert date: %s to time", dateInTime)
	}

	investmentConn := epifigrpc.NewConnByService(cfg.INVESTMENT_SERVICE)
	defer epifigrpc.CloseConn(investmentConn)
	filegeneratorClient := filegenerator.NewFileGeneratorClient(investmentConn)

	fileIDs := fetchFileDetails(filegeneratorClient, timestamppb.New(dateInTime))
	fileIDToFileContentMap := fetchFileContent(filegeneratorClient, fileIDs)

	for _, value := range fileIDToFileContentMap {
		f, err := os.Create(fmt.Sprintf("./%s", value.FileName))
		if err != nil {
			logger.Fatal(fmt.Sprintf("failed to create file with name: %s", value.FileName), zap.Error(err))
			return err
		}

		fileContentInString := string(value.FileContent)
		_, err = f.WriteString(fileContentInString)
		if err != nil {
			logger.Fatal(fmt.Sprintf("error while writing to the file with name: %s", value.FileName), zap.Error(err))
			_ = f.Close()
			return err
		}
		_ = f.Close()
	}
	return nil
}

func fetchFileDetails(filegeneratorClient filegenerator.FileGeneratorClient, dateInTimeStamp *timestamppb.Timestamp) []string {
	ctx := context.Background()
	fileDetails, err := filegeneratorClient.GetFileDetailsByDate(ctx, &filegenerator.GetFileDetailsByDateRequest{
		StartDate: dateInTimeStamp,
		EndDate:   dateInTimeStamp,
		FileType:  filegenerator.FileType_FILE_TYPE_CREDIT_MIS,
	})
	if err != nil {
		logger.Error(ctx, fmt.Sprintf("error while retrieving file details for date: %s", *date), zap.Error(err))
		os.Exit(1)
	}
	if !fileDetails.Status.IsSuccess() {
		logger.Error(ctx,
			fmt.Sprintf(" retrieving file details for date: %s was not successful with debugMessage: %s and short Message: %s",
				*date, fileDetails.Status.DebugMessage, fileDetails.Status.ShortMessage))
		os.Exit(1)
	}

	var fileIDs []string
	for _, fileDetail := range fileDetails.FileDetails {
		fileIDs = append(fileIDs, fileDetail.FileId)
	}
	return fileIDs
}

func fetchFileContent(filegeneratorClient filegenerator.FileGeneratorClient, fileIDs []string) map[string]*filegenerator.FileContent {
	ctxForFileContentFetch := context.Background()
	fileContent, err := filegeneratorClient.GetFileContent(ctxForFileContentFetch, &filegenerator.GetFileContentRequest{FileIds: fileIDs})
	if err != nil {
		logger.Error(ctxForFileContentFetch, fmt.Sprintf("error while retrieving file content for date: %s for filIDs: %s", *date, fileIDs), zap.Error(err))
		os.Exit(1)
	}
	if !fileContent.Status.IsSuccess() {
		logger.Error(ctxForFileContentFetch,
			fmt.Sprintf(" retrieving file content for date: %s was not successful with debugMessage: %s and short Message: %s",
				*date, fileContent.Status.DebugMessage, fileContent.Status.ShortMessage))
		os.Exit(1)
	}
	return fileContent.FileIdToContentMap

}
