""" Programa para gestão do catálogo de produtos.
Permite:
    - Listar o catálogo
    - Pesquisar por alguns campos
    - Eliminar um registo do catalogo
    - Guardar o catálogo em ficheiro
"""
from decimal import Decimal as dec
import re
from typing import TextIO


PRODUCT_TYPES = {
    "AL": "AlimentaÃ§Ã£o",
    "DL": "Detergentes p/ LoiÃ§a",
    "FRL": "Frutas e Legumes",
}

class Produto:
    # id, designacao,tipo/categoria,quantidade,preco unitÃ¡rio
    def __init__(
            self,
            id_: int,  # > 0 e cinco dÃ­gitos
            nome: str,  # pelo menos 2 palavras com pelo menos 2 cars.
            tipo: str,  # tipo sÃ³ pode ser 'AL', 'DL', 'FRL'
            quantidade: int,  # >= 0
            preco: dec,  # >= 0
    ):
        # 1. Validar parÃ¢metros
        if id_ <= 0 or len(str(id_)) != 5:
            raise InvalidProdAttr(f"{id_=} invÃ¡lido (deve ser > 0 e ter 5 dÃ­gitos)")

        if not valida_nome(nome):
            raise InvalidProdAttr(f"{nome=} invÃ¡lido")

        if tipo not in PRODUCT_TYPES:
            raise InvalidProdAttr(f"{tipo=}: tipo nÃ£o reconhecido.")

        if quantidade < 0:
            raise InvalidProdAttr(f"{quantidade=} invÃ¡lida (deve ser >= 0)")

        if preco < 0:
            raise InvalidProdAttr(f"{preco=} invÃ¡lido (deve ser >= 0)")

        # 2. Inicializar/definir o objecto
        self.id = id_
        self.nome = nome
        self.tipo = tipo
        self.quantidade = quantidade
        self.preco = preco
    #:

    @classmethod
    def from_csv(cls, csv: str) -> 'Produto':
        attrs = csv.split(',')
        return Produto(
            id_= int(attrs[0]),
            nome = attrs[1],
            tipo = attrs[2],
            quantidade = int(attrs[3]),
            preco = dec(attrs[4])
        )
    #:

    def __str__(self) -> str:
        return f'Produto[id: {self.id} nome: {self.nome}]'
    #:

    def __repr__(self) -> str:
        return f"Produto({self.id}, '{self.nome}', '{self.tipo}', {self.quantidade}, Decimal('{self.preco}'))"
    #:

    @property
    def desc_tipo(self) -> str:
        return PRODUCT_TYPES[self.tipo]
    #:
#:

def valida_nome(nome: str) -> bool:
    return bool(re.fullmatch(r"[a-zA-ZÃ£Ã³]{2,}(\s+[a-zA-ZÃ£Ã³]{2,})*", nome))
#:

class InvalidProdAttr(ValueError):
    """
    Invalid Product Attribute.
    """
#:

class ProductCollection:
    def __init__(self):
        self.produtos = []
    #:

    @classmethod
    def from_csv(cls, csv_path: str) -> 'ProductCollection':
        prods = ProductCollection()
        with open(csv_path, 'rt') as file:
            for line in relevant_lines(file):
                prods.append(Produto.from_csv(line))
        return prods
    #:

    def append(self, novo_prod: Produto):
        if self.search_by_id(novo_prod.id):
            raise DuplicateValue(f'Produto jÃ¡ existe com id {novo_prod.id}')
        self.produtos.append(novo_prod)
    #:

    def search_by_id(self, id_: int) -> Produto | None:
        for prod in self.produtos:
            if prod.id == id_:
                return prod
        return None
    #:

    def _dump(self):
        for prod in self.produtos:
            print(prod)
    #:
#:

def relevant_lines(file: TextIO):
    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue
        if line.startswith('#') or line.startswith('//') or line.startswith('##'):
            continue
        yield line   # TODO: remover '\n'
#:

class DuplicateValue(Exception):
    """
    If there is a duplicate product in a ProductCollection.
    """

def main():
    prods = ProductCollection.from_csv('produtos.csv')
    prods._dump()
#:

# def main():
#     # produtos = ler ficheiro 'produtos.csv'
#     try:
#         prod1 = Produto(
#             id_=30987,
#             nome="pÃ£o de milho",
#             tipo="AL",
#             quantidade=2,
#             preco=dec("1"),
#         )

#         prod2 = Produto(
#             id_=30098,
#             nome="Leite mimosa",
#             tipo="AL",
#             quantidade=10,
#             preco=dec("2"),
#         )

#         prod3 = Produto.from_csv('21109,fairy,DL,20,3')

#         produtos = ProductCollection()
#         produtos.append(prod1)
#         produtos.append(prod2)
#         produtos.append(prod3)
#         produtos.append(prod3)
        
#         produtos._dump()
    
#     except ValueError as ex:
#         print("Erro: atributo invÃ¡lido")
#         print(ex)
#     except DuplicateValue as ex:
#         print("Erro: produto duplicado")
#         print(ex)
# #:


if __name__ == "__main__":  # verifica se o script foi executado
    main()  # na linha de comandos