"""
The goal is to calculate the age in years based on the day, month, and year of birth and the current day, month, and year. 
Note the following: under normal conditions, the age is the difference between the current year and the year of birth. 

However, if the current month is less than the birth month, or the current month is equal to the birth month and the current day is less than the birth day, the age is the current year minus the birth year minus one.

INPUT 
birth date: entered as a str in the format YYYY MM DD 
current date: datetime.dateobtained with datetime.date.today
"""

import sys
from datetime import date


def birthDate1():
    # Get the birth date from the user
    birth_date = input("Enter your birth date (YYYY MM DD): ").split("-")

    birth_year = int(birth_date[0])
    birth_month = int(birth_date[1])
    birth_day = int(birth_date[2])

    actualDate = date.today()

    age = actualDate.year - birth_year
    if (
        actualDate.month < birth_month
        or actualDate.month == birth_month
        and actualDate.day < birth_day
    ):
        age -= 1
    print(f"Your age is {age} years old")


def birthDate2():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} YYYY MM DD")
        sys.exit(2)

    birth_year = int(sys.argv[0])
    birth_month = int(sys.argv[1])
    birth_day = int(sys.argv[2])

    actualDate = date.today()
    age = actualDate.year - birth_year
    if (
        actualDate.month < birth_month
        or actualDate.month == birth_month
        and actualDate.day < birth_day
    ):
        age -= 1
    print(f"Your age is {age} years old")


if __name__ == "__main__":
    birthDate1()
    # birthDate2()
