#Exercicio 1.2 - Somente Codigo

#Bilheteria de evento com apenas 1 evento
#1.Cadastrar nome de evento
#2.Vender ingressos(verificar se ha ingressos)
#3.Repor ingressos(quantidade>0)
#4.Ver ingresso disponiveis

evento = {
    "nome": "Show da Banda XYZ",
    "ingressos_disponiveis": 100
}

def ver_ingressos_disponiveis():
    print(f"\nEvento: {evento['nome']}")
    print(f"Ingressos disponíveis: {evento['ingressos_disponiveis']}")

def vender_ingressos():
    try:
        quantidade = int(input("Quantos ingressos deseja comprar? "))
        if quantidade <= 0:
            print("Quantidade inválida.")
        elif quantidade > evento['ingressos_disponiveis']:
            print("Ingressos insuficientes para essa venda.")
        else:
            evento['ingressos_disponiveis'] -= quantidade
            print(f"Venda realizada com sucesso! {quantidade} ingresso(s) vendido(s).")
    except ValueError:
        print("Digite um número válido.")

def repor_ingressos():
    try:
        quantidade = int(input("Quantos ingressos deseja adicionar? "))
        if quantidade <= 0:
            print("Quantidade inválida.")
        else:
            evento['ingressos_disponiveis'] += quantidade
            print(f"{quantidade} ingresso(s) adicionado(s) com sucesso.")
    except ValueError:
        print("Digite um número válido.")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Ver ingressos disponíveis")
        print("2. Vender ingressos")
        print("3. Repor ingressos")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ver_ingressos_disponiveis()
        elif opcao == "2":
            vender_ingressos()
        elif opcao == "3":
            repor_ingressos()
        elif opcao == "4":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida.")
