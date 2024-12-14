import sys
from decimal import Decimal as dec

from console_utils import accept, ask, show_msg, pause, cls
from product_management import (
    Product,
    PRODUCT_TYPES,
    ProductCollection,
    InvalidAttr,
)

PRODUCTS_CSV_PATH = "products.csv"
prods_collection = ProductCollection
prod = Product
prods_types: dict = PRODUCT_TYPES


# Main
def main():
    global prods_collection
    try:
        prods_collection = ProductCollection.import_from_csv(PRODUCTS_CSV_PATH)
        exec_menu()
    except InvalidAttr as ex:
        print("Erro ao carregar produtos")
        print(ex)
    except KeyboardInterrupt:
        exec_end()


#:
# Menu
def exec_menu():
    print("Menu Principal")
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

        option = ask("Opção: ")

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
def enter_menu(title: str):
    cls()
    show_msg(title.upper())
    print()


#:
# Products List
def exec_list_products():
    enter_menu("Produtos")
    products_table(prods_collection)
    print()
    pause()


# Get products from database
def products_table(products: ProductCollection):
    header = (
        f'{"ID":^8} | {"Nome":^26} | {"Tipo":^8} | {"Quantidade":^16} | {"Preço":^14}'
    )
    separator = f'{"-" * 9}+{"-" * 28}+{"-" * 10}+{"-" * 18}+{"-" * 16}'

    show_msg(header)
    show_msg(separator)
    for product in products:
        data_line = f"{product.id:^8} | {product.name:<26} | {product.prod_type:<8} | {product.qnty:>16} | {product.prod_price:>14.2f}€"
        show_msg(data_line)


#:
# Search by ID
def exec_search_by_id():
    enter_menu("Pesquisar por ID")
    id = accept(
        msg="Indique o id do produto a pesquisar: ",
        error_msg="ID {} inválido. Por favor, tente novamente.",
        convert_fn=int,
    )
    if product := prods_collection.search_by_id(id):
        show_msg(f"Produto encontrado: {product.name}")
        print()
        products_table(ProductCollection([product]))
    else:
        show_msg(f"Produto com o id {id} não encontrado.")

    print()
    pause()


#:
# Search by type
def exec_search_by_type():
    enter_menu("Pesquisar por tipo")
    type = accept(
        msg="Indique o tipo do produto a pesquisar: ",
        error_msg="Tipo {} inválido. Por favor, tente novamente.",
        check_fn=lambda product: product in PRODUCT_TYPES,
    )
    print()
    if products := prods_collection.search(lambda prod: prod.prod_type == type):
        show_msg("Foram encontrados os seguintes produtos:")
        print()
        products_table(ProductCollection(products))
    else:
        show_msg(f"Não foram encontrados produtos do tipo {type}")

    print()
    pause()


#:
def display_product_types():
    show_msg("┏━━━━━━━━ Tipos de Produtos ━━━━━━━━┓")
    for code, prod_type in prods_types.items():
        show_msg(f"   {code}   |   {prod_type}")
    show_msg("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")


#:
# Add product
def exec_add_product():
    enter_menu("Adicionar produto")
    new_prod_id = accept(
        msg="Indique o id do produto a adicionar: ",
        error_msg="ID {} inválido. Por favor, tente novamente.",
        check_fn=int,
    )
    if prods_collection.search_by_id(new_prod_id):
        show_msg(f"Produto com o id {new_prod_id} já existe.")
    else:
        prod.validate_id(new_prod_id)
        try:
            new_prod_name = accept(
                msg="Indique o nome do produto a adicionar: ",
                error_msg="Nome {} inválido. Por favor, tente novamente.",
            )
            prod.validate_name(new_prod_name)

            display_product_types()
            new_prod_type = accept(
                msg="Indique o tipo do produto a adicionar: ",
                error_msg="Tipo {} inválido. Por favor, tente novamente.",
                check_fn=lambda product: product in PRODUCT_TYPES,
            )
            prod.validate_product_type

            new_prod_qnty = accept(
                msg="Indique a quantidade do produto a adicionar: ",
                error_msg="Quantidade {} inválida. Por favor, tente novamente.",
                check_fn=int,
            )
            prod.validate_quantity(new_prod_qnty)

            new_prod_price = accept(
                msg="Indique o preço do produto a adicionar: ",
                error_msg="Preço {} inválido. Por favor, tente novamente.",
                check_fn=dec,
            )
            prod.validate_price(new_prod_price)

            new_product = Product(
                id_=new_prod_id,
                name=new_prod_name,
                prod_type=new_prod_type,
                qnty=new_prod_qnty,
                prod_price=new_prod_price,
            )
            prods_collection.append(new_product)

            # Save to file
            prods_collection.export_to_csv(PRODUCTS_CSV_PATH)
            print(f"Novo produto adicionado: {prods_collection._dump} ")
        except InvalidAttr as err:
            print(err)


#:
# Display product types
def display_product_types():
    show_msg("┏━━━━━━━━ Tipos de Produtos ━━━━━━━━┓")
    for code, prod_type in prods_types.items():
        show_msg(f"   {code}   |   {prod_type}")
        show_msg("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")


def exec_end():
    print("  O programa vai terminar...")
    sys.exit(0)


#:

# verifica se o script foi executado diretamente na linha de comandos
if __name__ == "__main__":
    main()
