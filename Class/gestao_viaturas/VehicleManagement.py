""" 
Program for managing the vehicle catalog. This program will allow: 
    - Listing the catalog 
    - Searching by some fields 
    - Deleting a record from the catalog 
    - Saving the catalog to a file
o Alternative constructor Vehicle, CSV
o Methods __str__
o Property year of the license plate
o VehicleCollection with I/O (but using a dictionary) """

from datetime import date
import re

# Validation functions
""" Validate a plate number """


def validate_plate(plate) -> bool:
    return bool(re.fullmatch(r"[0-9]{2}-[A-Z]{2}-[0-9]{2}", plate))


#:
def validate_plateV2(plate) -> bool:
    parts = plate.split("-")
    if len(parts) != 3:
        return False
    return (
        len(parts) == 3
        and (parts[0].isdigit() and len(parts[0]) == 2)
        and (parts[1].isalpha() and len(parts[1]) == 2 and parts[1] == parts[1].upper())
        and (parts[2].isdigit() and len(parts[2]) == 2)
    )


#:

""" Validate Brand """


def validate_brand(brand: str) -> bool:
    words = brand.split()
    return len(words) >= 1 and all(word.isalnum() for word in words)


#:


def validate_brandV2(brand: str) -> bool:
    words = brand.split()
    for word in words:
        if not word.isalnum():
            return False
    return True


#:

""" Validate Model """


def validate_model(model: str) -> bool:
    return validate_brand(model)


#:

""" Exceptions """


class InvalidAttribute(ValueError):
    """Invalid Attribute"""


#:


class Vehicle:
    def __init__(
        self,
        license_plate: str,  # license plate: DD-LL-DD Where D is for digit, L for letter
        brand: str,  # brand of the vehicle: should have one or more words
        model: str,  # model: same as brand
        vehicle_date: str,  # year of the vehicle in ISO format (YYYY-MM-DD)
    ):
        # 1. Validate
        if not validate_plate(license_plate):
            raise InvalidAttribute(f"License plate invalid: {license_plate}")
        if not validate_brand(brand):
            raise InvalidAttribute(f"Brand invalid: {brand}")
        if not validate_model(model):
            raise InvalidAttribute(f"Model invalid: {model}")

        # 2. Object Definition
        self.license_plate = license_plate
        self.brand = brand
        self.model = model
        try:
            dateInserted = date.fromisoformat(vehicle_date)
            self.year = dateInserted.year
            self.month = dateInserted.month
            self.day = dateInserted.day
        except ValueError:
            raise InvalidAttribute(f"Invalid date: {vehicle_date}")

    #:
    @property
    def vehicle_date(self) -> date:
        return date(self.year, self.month, self.day)

    #:


#:
def main():
    res = validate_brand("fiat punto")
    print(res)


if __name__ == "__main__":
    main()
