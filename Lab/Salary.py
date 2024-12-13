"""
Write a program to calculate the contribution to Social Security, IRS, and the union from the gross salary, which is an input attribute.
"""

from decimal import Decimal as dec


def calculate_contributions(gross_salary):
    # Defining contribution rates (these values are examples and may vary according to local regulations)
    social_security_rate = dec("11.5")
    irs_rate = dec("25")
    union_rate = dec("0.5")

    # Calculating contributions
    social_security_contribution = gross_salary * (social_security_rate / 100)
    irs_contribution = gross_salary * (irs_rate / 100)
    union_contribution = gross_salary * (union_rate / 100)

    # Calculating net salary
    net_salary = (
        gross_salary
        - social_security_contribution
        - irs_contribution
        - union_contribution
    )

    return {
        "Gross Salary": gross_salary,
        "Social Security Contribution": social_security_contribution,
        "IRS Contribution": irs_contribution,
        "Union Contribution": union_contribution,
        "Net Salary": net_salary,
    }


def main():
    # Getting the gross salary from the user
    gross_salary = dec(input("Enter your gross salary: "))

    # Calculating contributions
    contributions = calculate_contributions(gross_salary)

    # Printing the results
    print("------ Results ------")
    for key, value in contributions.items():
        print(f"{key}: {value:.2f}")
    return 1


if __name__ == "__main__":
    main()
