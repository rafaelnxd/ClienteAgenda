import tkinter as tk
from tkinter import simpledialog, messagebox
import tkinter.ttk as ttk
import json

def adicionar_cliente(agenda, produtos):
    nome = simpledialog.askstring("Adicionar Cliente", "Digite o nome do cliente:")
    if nome is None:
        return
    
    telefone = simpledialog.askstring("Adicionar Cliente", "Digite o telefone do cliente:")
    if telefone is None:
        return
    
    email = simpledialog.askstring("Adicionar Cliente", "Digite o email do cliente:")
    if email is None:
        return
    
    endereco = simpledialog.askstring("Adicionar Cliente", "Digite o endereço do cliente:")
    if endereco is None:
        return
    
    cpf = simpledialog.askstring("Adicionar Cliente", "Digite o CPF do cliente:")
    if cpf is None:
        return
    
    necessidade_especial = simpledialog.askstring("Adicionar Cliente", "Possui alguma deficiência ou necessidade especial?")
    if necessidade_especial is None:
        return
    
    produtos_interesse = simpledialog.askstring("Adicionar Cliente", "Digite os produtos de interesse (separados por vírgula):")
    if produtos_interesse is None:
        return

    produtos_interesse = [produto.strip() for produto in produtos_interesse.split(",")]

    produtos_invalidos = [produto for produto in produtos_interesse if produto not in produtos]
    if produtos_invalidos:
        messagebox.showwarning("Produtos Inválidos", f"Os seguintes produtos não existem: {', '.join(produtos_invalidos)}")
        return

    agenda[nome] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
        'cpf': cpf,
        'necessidade_especial': necessidade_especial,
        'produtos_interesse': produtos_interesse
    }

    salvar_clientes(agenda)
    mostrar_lista_clientes(agenda, produtos)
    messagebox.showinfo("Sucesso", f"Cliente {nome} adicionado com sucesso!")
    
def listar_cliente_interativo(agenda, produtos):
    root = tk.Tk()
    root.title("Lista de Clientes")
    
    popup_width = 1400
    popup_height = 300

 
    root.geometry(f"{popup_width}x{popup_height}")

    tree = ttk.Treeview(root)
    tree["columns"] = ("Telefone", "Email", "Endereço", "CPF", "Necessidade Especial", "Produtos de Interesse")

    tree.heading("#0", text="Nome")
    tree.heading("Telefone", text="Telefone")
    tree.heading("Email", text="Email")
    tree.heading("Endereço", text="Endereço")
    tree.heading("CPF", text="CPF")
    tree.heading("Necessidade Especial", text="Necessidade Especial")
    tree.heading("Produtos de Interesse", text="Produtos de Interesse")


    for nome, data in agenda.items():
        tree.insert("", "end", text=nome, values=(
            data.get('telefone', ''),
            data.get('email', ''),
            data.get('endereco', ''),
            data.get('cpf', ''),
            data.get('necessidade_especial', ''),
            ', '.join(data.get('produtos_interesse', []))
        ))

    tree.pack(expand=True, fill="both")

    def mostrar_detalhes():
        item = tree.focus()
        nome_cliente = tree.item(item, "text")
        mostrar_detalhes_cliente(agenda, nome_cliente)

    def adicionar_contato():
        adicionar_cliente(agenda, produtos)
        tree.delete(*tree.get_children())
        for nome, data in agenda.items():
            tree.insert("", "end", text=nome, values=(
                data.get('telefone', ''),
                data.get('email', ''),
                data.get('endereco', ''),
                data.get('cpf', ''),
                data.get('necessidade_especial', ''),
                ', '.join(data.get('produtos_interesse', []))
            ))

    def remover_contato():
        excluir_cliente(agenda)
        tree.delete(*tree.get_children())
        for nome, data in agenda.items():
            tree.insert("", "end", text=nome, values=(
                data.get('telefone', ''),
                data.get('email', ''),
                data.get('endereco', ''),
                data.get('cpf', ''),
                data.get('necessidade_especial', ''),
                ', '.join(data.get('produtos_interesse', []))
            ))

    def editar_contato():
        editar_cliente(agenda, produtos)
        tree.delete(*tree.get_children())
        for nome, data in agenda.items():
            tree.insert("", "end", text=nome, values=(
                data.get('telefone', ''),
                data.get('email', ''),
                data.get('endereco', ''),
                data.get('cpf', ''),
                data.get('necessidade_especial', ''),
                ', '.join(data.get('produtos_interesse', []))
            ))
            
        
    def procurar_contato():
        buscar_cliente(agenda)

    def sair():
        root.withdraw()
        return perguntar_outra_acao()
        
    
        

    button_mostrar_detalhes = tk.Button(root, text="Mostrar Detalhes", command=mostrar_detalhes)
    button_mostrar_detalhes.pack(side="left", padx=70)

    button_adicionar_contato = tk.Button(root, text="Adicionar Contato", command=adicionar_contato)
    button_adicionar_contato.pack(side="left", padx=70)

    button_remover_contato = tk.Button(root, text="Remover Contato", command=remover_contato)
    button_remover_contato.pack(side="left", padx=70)

    button_editar_contato = tk.Button(root, text="Editar Contato", command=editar_contato)
    button_editar_contato.pack(side="left", padx=70)

    button_procurar_contato = tk.Button(root, text="Procurar Contato", command=procurar_contato)
    button_procurar_contato.pack(side="left", padx=70)

    button_sair = tk.Button(root, text="Sair", command=sair)
    button_sair.pack(side="left", padx=70)
    
    root.mainloop()


def mostrar_detalhes_cliente(agenda, nome_cliente):
    if nome_cliente in agenda:
        data = agenda[nome_cliente]
        info = f"\nNome: {nome_cliente}\nTelefone: {data.get('telefone', '')}\nEmail: {data.get('email', '')}\nEndereço: {data.get('endereco', '')}\nCPF: {data.get('cpf', '')}"

        if 'necessidade_especial' in data:
            info += f"\nNecessidade Especial: {data['necessidade_especial']}"

        if 'produtos_interesse' in data:
            info += f"\nProdutos de Interesse: {', '.join(data['produtos_interesse'])}"

        messagebox.showinfo("Detalhes do Cliente", info)
    else:
        messagebox.showwarning("Cliente não encontrado", f"Cliente {nome_cliente} não encontrado.")
    

def listar_cliente(agenda, produtos):
    listar_cliente_interativo(agenda, produtos)

def editar_cliente(agenda, produtos):

    nome = simpledialog.askstring("Editar Cliente", "Digite o nome do cliente que deseja editar:")
    if nome is None:
        return

    if nome in agenda:
        opcao = simpledialog.askinteger("Editar Cliente", "Escolha a opção desejada:\n1. Editar telefone\n2. Editar email\n3. Editar endereço\n4. Editar CPF\n5. Editar necessidade especial\n6. Editar produtos de interesse", minvalue=1, maxvalue=6)

        if opcao is None:
            return

        if opcao == 1:
            agenda[nome]['telefone'] = simpledialog.askstring("Editar Cliente", "Digite o novo telefone:")
            if agenda[nome]['telefone'] is None:
                return
        elif opcao == 2:
            agenda[nome]['email'] = simpledialog.askstring("Editar Cliente", "Digite o novo email:")
            if agenda[nome]['email'] is None:
                return
        elif opcao == 3:
            agenda[nome]['endereco'] = simpledialog.askstring("Editar Cliente", "Digite o novo endereço:")
            if agenda[nome]['endereco'] is None:
                return
        elif opcao == 4:
            agenda[nome]['cpf'] = simpledialog.askstring("Editar Cliente", "Digite o novo CPF:")
            if agenda[nome]['cpf'] is None:
                return
        elif opcao == 5:
            agenda[nome]['necessidade_especial'] = simpledialog.askstring("Editar Cliente", "Digite a nova informação sobre necessidade especial:")
            if agenda[nome]['necessidade_especial'] is None:
                return
        elif opcao == 6:
            produtos_interesse = simpledialog.askstring("Editar Cliente", "Digite os novos produtos de interesse (separados por vírgula):")
            if produtos_interesse is None:
                return

            produtos_interesse = [produto.strip() for produto in produtos_interesse.split(",")]

        
            produtos_invalidos = [produto for produto in produtos_interesse if produto not in produtos]
            if produtos_invalidos:
                messagebox.showwarning("Produtos Inválidos", f"Os seguintes produtos não existem: {', '.join(produtos_invalidos)}")
                return

            agenda[nome]['produtos_interesse'] = produtos_interesse
        else:
            messagebox.showwarning("Opção Inválida", "Opção inválida")
    else:
        messagebox.showwarning("Cliente não encontrado", f"Cliente {nome} não encontrado.")

    salvar_clientes(agenda)
    mostrar_lista_clientes(agenda, produtos)
def excluir_cliente(agenda):
    nome = simpledialog.askstring("Excluir Cliente", "Digite o nome do cliente que deseja excluir (ou digite 'todos' para excluir todos os clientes):")
    if nome is None:
        return

    if nome.lower() == 'todos':
        confirmacao = messagebox.askyesno("Confirmar Exclusão", "Tem certeza que deseja excluir todos os clientes?")
        if confirmacao:
            agenda.clear()
            messagebox.showinfo("Sucesso", "Todos os clientes foram excluídos com sucesso!")
        return

    if nome in agenda:
        del agenda[nome]
        salvar_clientes(agenda)
        mostrar_lista_clientes(agenda)
        messagebox.showinfo("Sucesso", f"Cliente {nome} excluído com sucesso!")
    else:
        messagebox.showwarning("Cliente não encontrado", f"Cliente {nome} não encontrado.")
    
def buscar_cliente(agenda):
    nome = simpledialog.askstring("Buscar Cliente", "Digite o nome do cliente que deseja buscar:")
    if nome is None:
        return

    if nome in agenda:
        data = agenda[nome]
        info = f"\nNome: {nome}\nTelefone: {data['telefone']}\nEmail: {data['email']}\nEndereço: {data['endereco']}\nCPF: {data['cpf']}"
        messagebox.showinfo("Cliente Encontrado", info)
    else:
        messagebox.showwarning("Cliente não encontrado", f"Cliente {nome} não encontrado.")

def mostrar_lista_clientes(agenda, produtos):
    listar_cliente(agenda, produtos)

def salvar_clientes(agenda):
   with open('clientes.json', 'w') as file:
        json.dump(agenda, file)


def carregar_contatos():
    agenda = {}
    try:
        with open('clientes.json', 'r') as file:
            agenda = json.load(file)
    except FileNotFoundError:
        pass
    return agenda


def adicionar_produto(produtos):
    nome = simpledialog.askstring("Adicionar Produto", "Digite o nome do produto:")
    if nome is None:
        return
    
    descricao = simpledialog.askstring("Adicionar Produto", "Digite a descrição do produto:")
    if descricao is None:
        return
    
    preco = simpledialog.askfloat("Adicionar Produto", "Digite o preço do produto:")
    if preco is None:
        return
    
    produtos[nome] = {
        'descricao': descricao,
        'preco': preco
    }

    salvar_produtos(produtos)
    mostrar_lista_produtos(produtos)
    messagebox.showinfo("Sucesso", f"Produto {nome} adicionado com sucesso!")

def mostrar_detalhes_produto(produtos, nome_produto):
    if nome_produto in produtos:
        detalhes = f"Nome: {nome_produto}\nDescrição: {produtos[nome_produto]['descricao']}\nPreço: {produtos[nome_produto]['preco']}"
        messagebox.showinfo("Detalhes do Produto", detalhes)
    else:
        messagebox.showwarning("Produto não encontrado", f"Produto {nome_produto} não encontrado.")

def listar_produtos_interativo(produtos):
    root = tk.Tk()
    root.title("Lista de Produtos")

    tree = ttk.Treeview(root)
    tree["columns"] = ("Descrição", "Preço")

    tree.heading("#0", text="Nome")
    tree.heading("Descrição", text="Descrição")
    tree.heading("Preço", text="Preço")

    for nome, dados in produtos.items():
        tree.insert("", "end", text=nome, values=(dados["descricao"], dados["preco"]))

    tree.pack(expand=True, fill="both")

    def mostrar_detalhes():
        item = tree.focus()
        nome_produto = tree.item(item, "text")
        mostrar_detalhes_produto(produtos, nome_produto)

    def adicionar_novo_produto():
        adicionar_produto(produtos)
        tree.delete(*tree.get_children()) 
        for nome, dados in produtos.items():
            tree.insert("", "end", text=nome, values=(dados["descricao"], dados["preco"]))

    def remover_produto():
        excluir_produto(produtos)
        item = tree.focus()
        nome_produto = tree.item(item, "text")
        if nome_produto in produtos:
            del produtos[nome_produto]
            salvar_produtos(produtos)
            tree.delete(item)
    

    def sair():
        perguntar_outra_acao() 
        root.withdraw()
        
        
        

    button_mostrar_detalhes = tk.Button(root, text="Mostrar Detalhes", command=mostrar_detalhes)
    button_mostrar_detalhes.pack(side="left", padx=40)

    button_adicionar_produto = tk.Button(root, text="Adicionar Produto", command=adicionar_novo_produto)
    button_adicionar_produto.pack(side="left", padx=40)

    button_remover_produto = tk.Button(root, text="Remover Produto", command=remover_produto)
    button_remover_produto.pack(side="left", padx=40)

    button_sair = tk.Button(root, text="Sair", command=sair)
    button_sair.pack(side="left", padx=40)

    root.mainloop()


def mostrar_lista_produtos(produtos):
    listar_produtos_interativo(produtos)


def excluir_produto(produtos):
    nome = simpledialog.askstring("Excluir Produto", "Digite o nome do produto que deseja excluir:")
    if nome is None:
        return

    if nome in produtos:
        del produtos[nome]
        salvar_produtos(produtos)
        mostrar_lista_produtos(produtos)
        messagebox.showinfo("Sucesso", f"Produto {nome} excluído com sucesso!")
    else:
        messagebox.showwarning("Produto não encontrado", f"Produto {nome} não encontrado.")

def salvar_produtos(produtos):
    with open('produtos.j   son', 'w') as file:
        json.dump(produtos, file)

def carregar_produtos():
    produtos = {}
    try:
        with open('produtos.json', 'r') as file:
            produtos = json.load(file)
    except FileNotFoundError:
        pass
    return produtos

def perguntar_outra_acao():
    return messagebox.askyesno("Outra Ação", "Deseja realizar outra ação?")