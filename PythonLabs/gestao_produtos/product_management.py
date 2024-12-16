import re
from decimal import Decimal as dec
from typing import Iterable, TextIO

CSV_DELIM = ","
EXPECTED_CSV_COLUMNS = 5
PRODUCT_TYPES = {
    "AL": "Alimentação",
    "DL": "Detergentes p/ Loiça",
    "FRL": "Frutas e Legumes",
}


class Product:
    # Construtor
    def __init__(self, id_: int, name: str, prod_type: str, qnty: int, prod_price: dec):
        # Parameter validation
        self.validate_id(id_)
        self.validate_name(name)
        self.validate_product_type(prod_type)
        self.validate_quantity(qnty)
        self.validate_price(prod_price)

        # Initialize attributes
        self.id = id_
        self.name = name
        self.prod_type = prod_type
        self.qnty = qnty
        self.prod_price = prod_price

    # Read CSV
    @classmethod
    def read_csv(cls, csv: str, csv_delim=CSV_DELIM) -> "Product":
        attrs = csv.split(csv_delim)
        if len(attrs) != 5:
            raise InvalidAttr("O arquivo CSV deve ter 5 colunas")
        return Product(
            id_=int(attrs[0].strip()),
            name=attrs[1].strip(),
            prod_type=attrs[2].strip(),
            qnty=int(attrs[3].strip()),
            prod_price=dec(attrs[4].strip()),
        )

    #:
    def save_csv(self, csv_delim=CSV_DELIM) -> str:
        return csv_delim.join(
            (
                str(self.id),
                self.name,
                self.prod_type,
                str(self.qnty),
                str(self.prod_price),
            )
        )

    #:
    def __str__(self) -> str:
        return f"Produto[id: {self.id} nome: {self.name}]"

    #:

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        return f"{cls_name}({self.id}, '{self.name}', '{self.prod_type}', {self.quantity}, Decimal('{self.price}'))"

    #:

    # Comparison between 2 instances of the product class
    def __eq__(self, o) -> bool:
        if not isinstance(o, Product):
            return False
        return self.id == o.id

    #:

    @property
    def type_desc(self) -> str:
        return PRODUCT_TYPES[self.prod_type]

    #:

    @staticmethod
    def validate_id(id_: int):
        # Attempt to convert the input to an integer
        try:
            id_ = int(id_)
        except ValueError:
            raise InvalidAttr(f"{id_=} deve ser um número inteiro.")

        # Check if the ID is greater than 0
        if id_ <= 0:
            raise InvalidAttr(f"{id_=} inválido (deve ser > 0).")

        # Check if the ID has exactly 5 digits
        if id_ == len(str(id_)) != 5:
            raise InvalidAttr(f"{id_=} inválido (deve ter exatamente 5 dígitos).")

    @staticmethod
    def validate_name(name: str):
        if not Product.name_validation(name):
            raise InvalidAttr(f"Nome inválido: {name}")

    @staticmethod
    def validate_product_type(prod_type: str):
        if prod_type not in PRODUCT_TYPES:
            raise InvalidAttr(f"Tipo de produto inválido: {prod_type}")

    @staticmethod
    def validate_quantity(qnty):
        # Attempt to convert the input to an integer
        try:
            qnty = int(qnty)
        except ValueError:
            raise InvalidAttr(f"{qnty=} deve ser um número inteiro.")

        if qnty <= 0:
            raise InvalidAttr(f"Quantidade inválida: {qnty}")

    #:
    @staticmethod
    def validate_price(price):
        # Attempt to convert the input to a float
        try:
            price = dec(price)
        except ValueError:
            raise InvalidAttr(f"{price=} deve ser um número válido.")

        # Check if the price is non-negative
        if price < 0:
            raise InvalidAttr(f"{price=} inválido (deve ser >= 0).")

    @staticmethod
    def name_validation(name: str) -> bool:
        regex = "ñãàáâäåéèêęēëóõôòöōíîìïįīúüùûūÑÃÀÁÂÄÅÉÈÊĘĒËÓÕÔÒÖŌÍÎÌÏĮĪÚÜÙÛŪ"
        return bool(
            re.fullmatch(rf"[a-zA-Z{regex}]{{2,}}(\s+[a-zA-Z{regex}]{{2,}})*", name)
        )

    #:


class InvalidAttr(ValueError):
    """
    Invalid Product Attribute.
    """


#:


class DuplicateValue(Exception):
    """
    If there is a duplicate product in a ProductCollection.
    """


class ProductCollection:
    def __init__(self, initial_values: Iterable[Product] = ()):
        self._products: list[Product] = []
        for prod in initial_values:
            self.append(prod)

    #:
    def append(self, product: Product) -> None:
        if self.search_by_id(product.id):
            raise ValueError(f"Produto com o id {product.id} já existe.")
        self._products.append(product)

    #:

    # import and export to csv file
    def export_to_csv(self, csv_path: str, encoding="UTF-8"):
        if len(self._products) == 0:
            raise ValueError("Coleção Vazia")
        with open(csv_path, "wt", encoding=encoding) as file:
            for product in self._products:
                print(product.save_csv(), file=file)

    #:
    @classmethod
    def import_from_csv(self, csv_path: str, encoding="UTF-8") -> "ProductCollection":
        collection = ProductCollection()
        with open(csv_path, "rt", encoding=encoding) as file:
            for line in relevant_lines(file):
                collection.append(Product.read_csv(line))
        return collection

    #:
    def search_by_id(self, id: int) -> Product | None:
        for product in self._products:
            if product.id == id:
                return product
        return None

    #:
    def search(self, find_fn):
        for product in self._products:
            if find_fn(product):
                yield product

    #:
    def __len__(self) -> int:
        return len(self._products)

    #:
    def __iter__(self):
        for product in self._products:
            yield product

    #:
    def remove_by_id(self, id_: int) -> Product | None:
        product = self.search_by_id(id_)
        if product:
            self._products.remove(product)
        return product

    #:
    def _dump(self):
        for product in self._products:
            print(product)


#:


def relevant_lines(file: TextIO):
    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue
        if line.startswith("#"):
            continue
        yield line


#:
