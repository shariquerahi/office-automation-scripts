import pandas as pd

# Read the first CSV data
df1 = pd.read_csv('/Users/shariquerahi/Downloads/Early_Salary_Pending - Non_Disbused.csv', delimiter=',')  # Assuming your first CSV is tab-separated

# Read the second CSV data
df2 = pd.read_csv('/Users/shariquerahi/Downloads/Early_Salary - Our_Data_MI.csv')

# Merge the two dataframes on the common column "TRACK_ID" and "Error_track_id"
merged_df = pd.merge(df1, df2, left_on='Loan_ID', right_on='VENDOR_REQUEST_ID', how='inner')

# Display the result or perform further actions
print("Matched Data:")
print(merged_df)
merged_df.to_csv('/Users/shariquerahi/Desktop/Git/Python_Script/Gen_PythonScript/NON_DISBURSED_sTATUS.csv', index=False)
print("Matched data saved to 'matched_data.csv'")