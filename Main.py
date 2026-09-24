ARQUIVO = "medicamentos.csv"

def criar_arquivo():
    arquivo = open(ARQUIVO, "a")
    arquivo.write("")


def carregar_medicamentos():
    medicamentos = []

    arquivo = open(ARQUIVO, "r")

    for linha in arquivo:
        dados = linha.strip().split(",")

        medicamento = {
            "nome": dados[0],
            "categoria": dados[1],
            "quantidade": int(dados[2])}

        medicamentos.append(medicamento)

    return medicamentos


def salvar_medicamentos(medicamentos):
    arquivo = open(ARQUIVO, "w")

    for medicamento in medicamentos:
        arquivo.write(
            medicamento["nome"] + "," +
            medicamento["categoria"] + "," +
            str(medicamento["quantidade"]) + "\n")


def cadastrar_medicamento(medicamentos):
    print("\nCADASTRAR MEDICAMENTO\n")

    nome = input("Nome do medicamento: ")
    categoria = input("Categoria: ")
    quantidade = int(input("Quantidade em estoque: "))

    medicamento = {
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade}

    medicamentos.append(medicamento)

    print("\nMedicamento cadastrado com sucesso!")

    return medicamentos


def listar_medicamentos(medicamentos):
    print("\nMEDICAMENTOS CADASTRADOS ")

    contador = 1

    for medicamento in medicamentos:
        print("\nMedicamento", contador)
        print("Nome:", medicamento["nome"])
        print("Categoria:", medicamento["categoria"])
        print("Quantidade em estoque:", medicamento["quantidade"])

        contador = contador + 1

    return medicamentos


def buscar_medicamento(medicamentos, nome_busca):
    encontrados = []

    for medicamento in medicamentos:
        if medicamento["nome"].lower() == nome_busca.lower():
            encontrados.append(medicamento)

    return encontrados


def realizar_busca(medicamentos):
    print("\nBUSCAR MEDICAMENTO\n")

    nome_busca = input("Digite o nome do medicamento: ")

    encontrados = buscar_medicamento(medicamentos, nome_busca)

    if encontrados == []:
        print("Medicamento não encontrado.")
    else:
        for medicamento in encontrados:
            print("\nMEDICAMENTO ENCONTRADO\n")
            print("Nome:", medicamento["nome"])
            print("Categoria:", medicamento["categoria"])
            print("Quantidade em estoque:", medicamento["quantidade"])

    return encontrados


def mostrar_menu():
    print("\nSISTEMA DE MEDICAMENTOS\n")
    print("1 - Cadastrar medicamento")
    print("2 - Listar medicamentos")
    print("3 - Buscar medicamento")
    print("4 - Sair\n")


def main():
    criar_arquivo()

    medicamentos = carregar_medicamentos()

    while True:
        mostrar_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            medicamentos = cadastrar_medicamento(medicamentos)

        elif opcao == "2":
            listar_medicamentos(medicamentos)

        elif opcao == "3":
            realizar_busca(medicamentos)

        elif opcao == "4":
            salvar_medicamentos(medicamentos)

            print("\nDados salvos com sucesso!")
            print("Programa encerrado.\n")
            break

        else:
            print("Opção inválida.")


main()
