from datetime import date
import re


class Viatura:

    def __init__(
        self,
        matricula: str,  # matricula: DD-LL-DD onde D: DÃ­gito L: Letra
        marca: str,  # marca: deve ter uma ou mais palavras (apenas letras ou dÃ­gitos)
        modelo: str,  # modelo: mesmo que a marca
        data: str,  # data: deve vir no formato ISO: 'YYYY-MM-DD'
    ):
        # 1. Validar
        if not valida_matricula(matricula):
            raise InvalidAttr(f"Matrícula inválida: {matricula}")

        if not valida_marca(marca):
            raise InvalidAttr(f"Marca inválida: {marca}")

        if not valida_modelo(modelo):
            raise InvalidAttr(f"Modelo inválida: {modelo}")

        # 2. Definir objecto
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        try:
            dt = date.fromisoformat(data)
            self.ano = dt.year
            self.mes = dt.month
            self.dia = dt.day
        except ValueError:
            raise InvalidAttr(f"Data invÃ¡lida: {data}")

    #:

    @property
    def data(self) -> date:
        return date(self.ano, self.mes, self.dia)


#:


def valida_matricula(matricula: str) -> bool:
    return bool(re.fullmatch(r"[0-9]{2}-[A-Z]{2}-[0-9]{2}", matricula))


#:


def valida_matricula2(matricula: str) -> bool:
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


def valida_marca(marca: str) -> bool:
    """
    Uma ou mais palavras alfanumÃ©ricas
    """
    palavras = marca.split()
    return len(palavras) >= 1 and all(palavra.isalnum() for palavra in palavras)


#:

# def valida_marca(marca: str) -> bool:
#     """
#     Uma ou mais palavras alfanumÃ©ricas
#     """
#     palavras = marca.split()
#     for palavra in palavras:
#         if not palavra.isalnum():
#             return False
#     return True
# #:


def valida_modelo(modelo):
    return valida_marca(modelo)


#:


class InvalidAttr(ValueError):
    """
    Invalid Product Attribute.
    """


#:

"""
EXPRESSÃ•ES LISTA

nums = [20, -30, 40, 50, 60, -2, -1, 40]
txt = 'Estamos a aprender expressÃµes lista e outras...'

positivos = []
for num in nums:
    if num > 0:
        positivos.append(num)

dobros = []
for num in nums:
    dobros.append(2 * num)

# expressÃ£o lista: [EXPRESSAO(VAR) for VAR in ITERÃVEL [if CONDICAO(VAR)]]
positivos = [num for num in nums if num > 0]  # SELECT num FROM nums WHERE num > 0
dobros = [2 * num for num in nums]            # SELECT 2 * num FROM nums
dobro_positivos = [2 * num for num in nums if num > 0] 

vogais = [ch for ch in txt if ch in 'aeiouAEIOU']
vogais_unicas = {ch for ch in txt if ch in 'aeiouAEIOU'}

todos_divisiveis_por_dez = True
for num in nums:
    if num % 10 != 0:
        todos_divisiveis_por_dez = False
print(f"Todos divisiveis por 10? {todos_divisiveis_por_dez}")

all([True, False, True])
"""
