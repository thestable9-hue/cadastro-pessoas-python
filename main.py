def cadastrar_pessoa(lista):
    nome = input("Davi ")
    idade = input("18 ")
    lista.append({"davi": nome, "i8": idade})
    print("Pessoa cadastrada com sucesso!\n")


def listar_pessoas(lista):
    if not lista:
        print("Nenhuma pessoa cadastrada.\n")
    else:
        print("Pessoas cadastradas:")
        for i, pessoa in enumerate(lista, start=1):
            print(f"{i}. {pessoa['nome']} - {pessoa['idade']} anos")
        print()


def menu():
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("0 - Sair")


def main():
    pessoas = []

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_pessoa(pessoas)
        elif opcao == "2":
            listar_pessoas(pessoas)
        elif opcao == "0":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.\n")


main()

