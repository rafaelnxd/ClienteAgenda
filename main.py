from packages.agenda_functions import *


def main():
    agenda = carregar_contatos()
    produtos = carregar_produtos()

    while True:
        menu = """
        Agenda de Clientes e Produtos\n
         1. - Listar Clientes
         2. - Listar Produtos
         3. - Sair
        """
        user_op = simpledialog.askinteger("Menu", menu + "\nDigite a opção desejada:", minvalue=1, maxvalue=3)

        if user_op == 1:
            listar_cliente_interativo(agenda, produtos)
        elif user_op == 2:
            mostrar_lista_produtos(produtos)
        elif user_op == 3:
            salvar_clientes(agenda)
            salvar_produtos(produtos)
            break

        outra_acao = perguntar_outra_acao()

        if not outra_acao:
            salvar_clientes(agenda)
            salvar_produtos(produtos)
            break

if __name__ == "__main__":
    main()
