""" 
PROBLEM DEFINITION: Given the gross salary value, this program breaks down the amounts for Social Security, IRS, and a specific union.
PROBLEM DESCRIPTION: The program receives the gross salary from standard input and then calculates and displays the following values in a user-friendly manner:
    - Contribution to Social Security (SS)
    - Taxes withheld for IRS
    - Contribution to the union
    - Resulting net salary

INPUTS: 
    - gross_salary -> Salary before deductions, 
    - data type: decimal.Decimal

The following parameters are constants for this program: 
    - SS_RATE -> Worker's contribution, 11.5%, value in %, decimal.Decimal 
    - IRS_RATE -> Withholding applied to the worker, 25%, value in %, decimal.Decimal 
    - UNION_CONTRIBUTION -> Contribution to the union, 0.5%, value in %, decimal.Decimal

OUTPUTS: 
    - ss_amount -> Amount for Social Security, decimal.Decimal 
    - ss_amount = gross_salary * (SS_RATE/100) This amount and the others are displayed in STDOUT with 2 decimal places. 
    - irs_amount -> IRS withholding, decimal.Decimal 
    - irs_amount = gross_salary * (IRS_RATE/100) 
    - union_amount -> Contribution (amount) to the union, decimal.Decimal 
    - union_amount = gross_salary * (UNION_CONTRIBUTION/100) 
    - net_salary -> gross_salary minus the deductions, decimal.Decimal 
    - net_salary = gross_salary - ss/irs/union amounts
"""

from decimal import Decimal as dec

SS_RATE = dec("11.5")
IRS_RATE = dec("25.0")
UNION_CONTRIBUTION = dec("0.5")

# Read the gross salary from standard input
gross_salary = dec(input("Enter the gross salary: "))

# Calculate the deductions
ss_amount = gross_salary * (SS_RATE / 100)
irs_amount = gross_salary * (IRS_RATE / 100)
union_amount = gross_salary * (UNION_CONTRIBUTION / 100)
net_salary = gross_salary - ss_amount - irs_amount - union_amount

# Print to console
print(f"Social Security: ${ss_amount:7.2f}")
print(f"IRS: ${irs_amount:7.2f}")
print(f"Union: ${union_amount:7.2f}")
print(f"Net Salary: ${net_salary:7.2f}")
