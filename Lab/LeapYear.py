import sys

# Verify if it's a Leap Year
year = int(input("Enter the year: "))
if year < 0:
    print(f"Invalid {year}")
    sys.exit(1)

if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
