#Exercicio 2 - Código e diagrama
#Sistema de Cadastros de Pacientes
#1- Cadastrar paciente
#2- Mostrar paciente cadastrado
#3- Atender Paciente
#4- Sair

# Lista para armazenar os pacientes
fila_pacientes = []

def cadastrar_paciente():
    nome = input("Nome do paciente: ")
    idade = input("Idade: ")
    sintomas = input("Sintomas: ")
    
    paciente = {
        "nome": nome,
        "idade": idade,
        "sintomas": sintomas
    }
    
    fila_pacientes.append(paciente)
    print(f"\n✅ Paciente '{nome}' cadastrado com sucesso!\n")

def mostrar_pacientes():
    if not fila_pacientes:
        print("\n⚠️ Nenhum paciente cadastrado.\n")
        return

    print("\n📋 Pacientes cadastrados:")
    for i, paciente in enumerate(fila_pacientes, start=1):
        print(f"{i}. Nome: {paciente['nome']}, Idade: {paciente['idade']}, Sintomas: {paciente['sintomas']}")
    print()

def atender_paciente():
    if not fila_pacientes:
        print("\n⚠️ Nenhum paciente para atender.\n")
        return

    paciente_atendido = fila_pacientes.pop(0)
    print(f"\n🩺 Atendendo paciente: {paciente_atendido['nome']}\n")

def menu():
    while True:
        print("=== SISTEMA DE CADASTRO DE PACIENTES ===")
        print("1. Cadastrar paciente")
        print("2. Mostrar pacientes cadastrados")
        print("3. Atender paciente")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_paciente()
        elif opcao == '2':
            mostrar_pacientes()
        elif opcao == '3':
            atender_paciente()
        elif opcao == '4':
            print("\n👋 Encerrando o sistema. Até mais!")
            break
        else:
            print("\n❌ Opção inválida. Tente novamente.\n")