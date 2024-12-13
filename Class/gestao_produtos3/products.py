"""
Programa para gestão do catálogo de produtos. Este programa permite:
    - Listar o catálogo
    - Pesquisar por alguns campos 
    - Eliminar um registo do catálogo
    - Guardar o catálogo em ficheiro
"""

from decimal import Decimal as dec
import re
from typing import TextIO


CSV_DELIM = ","
PRODUCT_TYPES = {
    "AL": "Alimentação",
    "DL": "Detergentes p/ Loiça",
    "FRL": "Frutas e Legumes",
}


class Produto:
    # id, designacao,tipo/categoria,quantidade,preco unitário
    def __init__(
        self,
        id_: int,  # > 0 e cinco dígitos
        name: str,  # pelo menos 2 palavras com pelo menos 2 cars.
        prod_type: str,  # tipo só pode ser 'AL', 'DL', 'FRL'
        quantity: int,  # >= 0
        price: dec,  # >= 0
    ):
        # 1. Validar parâmetros
        if id_ <= 0 or len(str(id_)) != 5:
            raise InvalidProdAttr(f"{id_=} inválido (deve ser > 0 e ter 5 dígitos)")

        if not valida_nome(name):
            raise InvalidProdAttr(f"{name=} inválido")

        if prod_type not in PRODUCT_TYPES:
            raise InvalidProdAttr(f"{prod_type=}: tipo não reconhecido.")

        if quantity < 0:
            raise InvalidProdAttr(f"{quantity=} inválida (deve ser >= 0)")

        if price < 0:
            raise InvalidProdAttr(f"{price=} inválido (deve ser >= 0)")

        # 2. Inicializar/definir o objecto
        self.id = id_
        self.name = name
        self.prod_type = prod_type
        self.quantity = quantity
        self.price = price

    #:

    @classmethod
    def from_csv(cls, csv: str, csv_delim=CSV_DELIM) -> "Produto":
        attrs = csv.split(csv_delim)
        return Produto(
            id_=int(attrs[0]),
            name=attrs[1],
            prod_type=attrs[2],
            quantity=int(attrs[3]),
            price=dec(attrs[4]),
        )

    #:

    def __str__(self) -> str:
        return f"Produto[id: {self.id} nome: {self.name}]"

    #:

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        return f"{cls_name}({self.id}, '{self.name}', '{self.prod_type}', {self.quantity}, Decimal('{self.price}'))"

    #:

    @property
    def desc_tipo(self) -> str:
        return PRODUCT_TYPES[self.prod_type]

    #:


#:


def valida_nome(nome: str) -> bool:
    com_acento = "ñãàáâäåéèêęēëóõôòöōíîìïįīúüùûūÑÃÀÁÂÄÅÉÈÊĘĒËÓÕÔÒÖŌÍÎÌÏĮĪÚÜÙÛŪ"
    return bool(
        re.fullmatch(
            rf"[a-zA-Z{com_acento}]{{2,}}(\s+[a-zA-Z{com_acento}]{{2,}})*", nome
        )
    )


#:


class InvalidProdAttr(ValueError):
    """
    Invalid Product Attribute.
    """


#:


class ProductCollection:
    def __init__(self):
        self._produtos: list[Produto] = []

    #:

    @classmethod
    def from_csv(cls, csv_path: str) -> "ProductCollection":
        prods = ProductCollection()
        with open(csv_path, "rt") as file:
            for line in relevant_lines(file):
                prods.append(Produto.from_csv(line))
        return prods

    #:

    def append(self, novo_prod: Produto):
        if self.search_by_id(novo_prod.id):
            raise DuplicateValue(f"Produto já existe com id {novo_prod.id}")
        self._produtos.append(novo_prod)

    #:

    def search_by_id(self, id_: int) -> Produto | None:
        for prod in self._produtos:
            if prod.id == id_:
                return prod
        return None

    #:

    def __iter__(self):
        for prod in self._produtos:
            yield prod

    def _dump(self):
        for prod in self._produtos:
            print(prod)

    #:


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


class DuplicateValue(Exception):
    """
    If there is a duplicate product in a ProductCollection.
    """
