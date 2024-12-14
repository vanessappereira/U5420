import sys

from products import PRODUCT_TYPES, ProductCollection, InvalidProdAttr, Product
from console_utils import accept, ask, show_msg, pause, cls


PRODUCTS_CSV_PATH = "products.csv"
prods_collection: ProductCollection
prods_types: dict = PRODUCT_TYPES


def main():
    global prods_collection
    try:
        prods_collection = ProductCollection.from_csv(PRODUCTS_CSV_PATH)
        exec_menu()
    except InvalidProdAttr as ex:
        print("Erro ao carregar produtos")
        print(ex)
    except KeyboardInterrupt:
        exec_end()


#:


def exec_menu():
    print("MENU PRINCIPAL")
    while True:
        cls()
        print()
        show_msg("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        show_msg("┃   L  - Listar catálogo                    ┃")
        show_msg("┃   P  - Pesquisar por id                   ┃")
        show_msg("┃   PT - Pesquisar por tipo                 ┃")
        show_msg("┃   A  - Acrescentar produto                ┃")
        show_msg("┃   E  - Eliminar produto                   ┃")
        show_msg("┃   G  - Guardar catálogo em ficheiro       ┃")
        show_msg("┃                                           ┃")
        show_msg("┃   T  - Terminar programa                  ┃")
        show_msg("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        print()

        option = ask("OPÇÃO: ")

        match option.upper():
            case "L" | "LISTAR":
                exec_list_products()
            case "P" | "PESQUISAR":
                exec_search_by_id()
            case "PT" | "TIPO":
                exec_search_by_type()
            case "A" | "ACRESCENTAR":
                exec_add_product()
            case "E" | "ELIMINAR":
                exec_remove_product()
            case "G" | "GUARDAR":
                exec_save_products()
            case "T" | "TERMINAR":
                exec_end()
            case _:
                print("Opção inválida")


#:


def exec_list_products():
    enter_menu("PRODUTOS")
    show_table_with_prods(prods_collection)
    print()
    pause()


#:


def exec_search_by_id():
    enter_menu("PESQUISAR POR ID")
    id_ = accept(
        msg="Indique o ID do produto a pesquisar: ",
        error_msg="ID {} inválido! Tente novamente.",
        convert_fn=int,
    )

    if prod := prods_collection.search_by_id(id_):
        show_msg("Produto encontrado.")
        print()
        show_table_with_prods(ProductCollection([prod]))
    else:
        show_msg(f"Produto com ID {id_} não encontrado.")

    print()
    pause()


#:
def exec_search_by_type():
    enter_menu("PESQUISA POR TIPO")
    prod_type = accept(
        msg="Indique o tipo do produto a pesquisar: ",
        error_msg="Tipo {} inválido! Tente novamente",
        check_fn=lambda prod: prod in PRODUCT_TYPES,
    )
    print()

    if prods := prods_collection.search(lambda prod: prod.prod_type == prod_type):
        show_msg("Foram encontrados os seguintes produtos:")
        print()
        show_table_with_prods(ProductCollection(prods))
    else:
        show_msg(f"Não foram encontrados produtos com tipo {prod_type}.")

    print()
    pause()


#:
def display_product_types():
    show_msg("┏━━━━━━━━ Tipos de Produtos ━━━━━━━━┓")
    for code, prod_type in prods_types.items():
        show_msg(f"   {code}   |   {prod_type}")
    show_msg("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")


def exec_add_product():
    enter_menu("ADICIONAR PRODUTO")

    prod_id = accept(
        msg="Indique o ID do produto a adicionar: ",
        error_msg="ID {} inválido! Tente novamente.",
        convert_fn=int,
    )

    if prods_collection.search_by_id(prod_id):
        show_msg("Produto já existe!")
        pause()
        return
    else:
        prod_name = accept(
            msg="Indique o nome do produto: ",
            error_msg="Nome {} inválido! Tente novamente",
        )

        display_product_types()
        prod_type = accept(
            msg="Indique o tipo do produto: ",
            error_msg="Tipo {} inválido! Tente novamente",
            check_fn=lambda prod: prod in PRODUCT_TYPES,
        )

        prod_quantity = accept(
            msg="Indique a quantidade do produto: ",
            error_msg="Quantidade {} inválida! Tente novamente",
            convert_fn=int,
        )

        prod_price = accept(
            msg="Indique o preço do produto: ",
            error_msg="Preço {} inválido! Tente novamente",
            convert_fn=float,
        )
    # create a new product with the given data
    new_product = Product(
        id_=prod_id,
        name=prod_name,
        prod_type=prod_type,
        quantity=prod_quantity,
        price=prod_price,
    )
    #:
    prods_collection.append(new_product)
    # Guardar no CSV

    show_msg("Produto adicionado com sucesso!")
    pause()


#:


#:
def enter_menu(title: str):
    cls()
    show_msg(title.upper())
    print()


#:


def exec_end():
    print("  O programa vai terminar...")
    sys.exit(0)


#:


def show_table_with_prods(prods: ProductCollection):
    header = (
        f'{"ID":^8} | {"Nome":^26} | {"Tipo":^8} | {"Quantidade":^16} | {"Preço":^14}'
    )
    sep = f'{"-" * 9}+{"-" * 28}+{"-" * 10}+{"-" * 18}+{"-" * 16}'

    show_msg(header)
    show_msg(sep)

    for prod in prods:
        data_line = f"{prod.id:^8} | {prod.name:<26} | {prod.prod_type:<8} | {prod.quantity:>16} | {prod.price:>14.2f}€"
        show_msg(data_line)


#:


if __name__ == "__main__":  # verifica se o script foi executado
    main()  # na linha de comandos
