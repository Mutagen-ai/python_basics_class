#File_handling_checkpoint
import numpy as np

# opening the file and closing it
file = open("Loan_prediction_dataset.csv", "r")
file.close()

# loading the LoanAmount column using genfromtxt
# usecols=8 targets the LoanAmount column directly
loan_amounts = np.genfromtxt(
    "Loan_prediction_dataset.csv",
    delimiter=",",
    skip_header=1,
    usecols=8,
    encoding="utf-8"
)

# Removing rows that do not have loan amounts
loan_amounts = loan_amounts[~np.isnan(loan_amounts)]

mean   = np.mean(loan_amounts)
median = np.median(loan_amounts)
std    = np.std(loan_amounts)

print(f"Total records with valid loan amounts: {len(loan_amounts)}")
print()
print("Loan Amount Statistics")
print("----------------------")
print(f"Mean:               {mean:.2f}")
print(f"Median:             {median:.2f}")
print(f"Standard Deviation: {std:.2f}")
print(f"Min:                {np.min(loan_amounts):.2f}")
print(f"Max:                {np.max(loan_amounts):.2f}")