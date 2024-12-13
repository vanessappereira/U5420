import sys

from products import ProductCollection, InvalidProdAttr
from console_utils import accept, ask, show_msg, pause, cls


PRODUCTS_CSV_PATH = "products.csv"
prods_collection: ProductCollection


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

        option = ask("  OPÇÃO> ")

        match option.upper():
            case "L" | "LISTAR":
                exec_list_products()
            case "P" | "PESQUISAR":
                exec_search_by_id()
            case "T" | "TERMINAR":
                exec_end()
            case _:
                print("Opção inválida")


#:


def exec_list_products():
    print("  PRODUTOS")
    show_table_with_prods(prods_collection)
    print()
    pause()


#:


def exec_search_by_id():
    print("  PESQUISAR POR ID")


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
