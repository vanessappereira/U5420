""" 
Programa para gestão de catalogo de viaturas. Programa permite:
- Listar o catalogo
- Pesquisar por alguns campos
- Eliminar um registo
- Guardar o catalog

# matricula: DD-LL-DD onde D:Dígito L: Letra
# marca:deve ter uma ou mais palavras
# modelo: mesmo que a marca
# data: deve vir formatado no formato ISO: YYYY-MM-DD
"""

from datetime import date
import re


class Viatura:
    def __init__(
        self,
        matricula: str,
        marca: str,
        modelo: str,
        data: str,
    ):
        # 1. Validar
        if not valida_matricula(matricula):
            raise InvalidAttr(f"Matricula inválida: {matricula}")
        if not valida_marca(marca):
            raise InvalidAttr(f"Marca inválida: {marca}")

        # 2. Definir objecto


#: Validadores
def valida_matricula(matricula: str) -> bool:
    partes = matricula.split("-")
    return (
        len(partes) == 3
        and (partes[0].isdigit() and len(partes[0]) == 2)
        and (
            partes[1].isalpha()
            and len(partes[1]) == 2
            and partes[1] == partes[1].upper()
        )
        and (partes[2].isdigit() and len(partes[2]) == 2)
    )


#:


def valida_matricula2(matricula: str) -> bool:
    return bool(re.fullmatch(r"[0-9]{2}-[A-Z]{2}-[0-9]{2}", matricula))


def valida_marca(marca: str) -> bool:
    palavras = marca.split()
    return len(palavras) >= 1 and all(palavras.isalnum for palavra in palavras)


# Excepções
class InvalidAttr(ValueError):
    """Atributo inválido"""
