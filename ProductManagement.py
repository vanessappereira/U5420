""" 
Program for managing products catalog. This program will allow: 
    - Listing the catalog 
    - Searching by some fields 
    - Deleting a record from the catalog 
    - Saving the catalog to a file
"""

import re
from typing import TextIO
from decimal import Decimal as dec

PRODUCT_TYPES = {
    "F": "Food",
    "WD": "Wash Detergents",
    "FV": "Fruits and Vegetables",
}
""" Validate name """


def validate_name(name: str) -> bool:
    return bool(re.fullmatch(r"^[a-zA-Z]{2,}(\s+[a-zA-Z]{2,})*$", name))


""" Exceptions """


class InvalidAttribute(ValueError):
    """Invalid Attribute"""


#:
class DuplicateValue(Exception):
    """
    If there is a duplicate product in a ProductCollection.
    """


class Product:
    # id, designation, type, quantity, unit price
    def __init__(
        self,
        id_: int,  # > 0 e 5 digits
        name: str,  # at least 2 words with minimum 2 chars
        type: str,  # type: F, WD, FV
        quantity: int,  # >= 0
        unit_price: dec,  # > 0
    ):
        # 1. Validate
        if id_ <= 0 or len(str(id_)) != 5:
            raise InvalidAttribute(
                f"Invalid id: {id_=}, should be between 1 and 5 digits"
            )
        if not validate_name(name):
            raise InvalidAttribute(f"Invalid name: {name=}")
        if type not in PRODUCT_TYPES:
            raise InvalidAttribute(f"Invalid type (not recognized): {type=}")
        if quantity < 0:
            raise InvalidAttribute(f"Invalid quantity: {quantity=}, should be >= 0")
        if unit_price <= 0:
            raise InvalidAttribute(f"Invalid unit price: {unit_price=}, should be > 0")

        # 2. Assign
        self.id = id_
        self.name = name
        self.type = type
        self.quantity = quantity
        self.unit_price = unit_price

        #:

    @classmethod
    def from_csv(cls, csv: str) -> "Product":
        attrs = csv.split(",")
        return Product(
            id_=int(attrs[0]),
            name=attrs[1],
            type=attrs[2],
            quantity=int(attrs[3]),
            unit_price=dec(attrs[4]),
        )

    #:
    def __str__(self) -> str:
        return f"Product[id: {self.id} name: {self.name}]"

    #:
    @property
    def desc_type(self) -> str:
        return PRODUCT_TYPES[self.type]

    #:
#:
""" Product Collections """


class ProductCollections:
    def __init__(self):
        self.products = []

    #:
    @classmethod
    def from_csv(cls, csv_path: str) -> "ProductCollections":
        prods = ProductCollections()
        with open(csv_path, "rt") as file:
            for line in relevant_lines(file):
                prods.append(Product.from_csv(line))
        return prods

    #:

    def append(self, new_product: Product):
        if self.search_by_id(new_product.id):
            raise DuplicateValue(f"Product with id {new_product.id} already exists")
        self.products.append(new_product)

    #:

    def search_by_id(self, id_: int) -> Product | None:
        for product in self.products:
            if product.id == id_:
                return product
        return None

    def _dump(self):
        for product in self.products:
            print(product)

    #:


def relevant_lines(file: TextIO):
    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue
        if line.startswith("#") or line.startswith("//") or line.startswith("##"):
            continue
        yield line
#:


def main():
    prods = ProductCollections.from_csv("produtos.csv")
    prods._dump()


#:

if __name__ == "__main__":  # verifica se o script foi executado
    main()  # na linha de comandos
