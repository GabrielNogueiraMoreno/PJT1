from auth import registrar, login
from crud import criar_produto, listar_produtos, atualizar_produto, deletar_produto

print("1 - Registrar")
print("2 - Login")

op = input("Escolha: ")

if op == "1":
    user = input("Usuário: ")
    senha = input("Senha: ")
    registrar(user, senha)
    print("Usuário criado!")

elif op == "2":
    user = input("Usuário: ")
    senha = input("Senha: ")

    if login(user, senha):
        print("Login realizado!")

        while True:
            print("\n1 - Criar produto")
            print("2 - Listar produtos")
            print("3 - Atualizar produto")
            print("4 - Deletar produto")
            print("0 - Sair")

            escolha = input(">> ")

            if escolha == "1":
                nome = input("Nome: ")
                preco = float(input("Preço: "))
                criar_produto(nome, preco)

            elif escolha == "2":
                produtos = listar_produtos()
                for p in produtos:
                    print(p)

            elif escolha == "3":
                id = int(input("ID: "))
                nome = input("Novo nome: ")
                preco = float(input("Novo preço: "))
                atualizar_produto(id, nome, preco)

            elif escolha == "4":
                id = int(input("ID: "))
                deletar_produto(id)

            elif escolha == "0":
                break

    else:
        print("Login inválido")