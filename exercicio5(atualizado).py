#exercicio 5
agendamentos = []
clientes = []

def agendar_servico():
    print("Seja bem-vindo ao agendamento de serviços!")
    nome = input("Qual seu nome? ")
    telefone = input("Qual seu telefone? ")
    data = input("Marcar data (dd/mm/aaaa): ")
    corte = input("Personalize seu corte: ")
    horario = input("Marcar horário (hh:mm): ")

    agendamento = {
        "nome": nome,
        "telefone": telefone,
        "data": data,
        "corte": corte,
        "horario": horario
    }
    agendamentos.append(agendamento)
    print("Serviço agendado com sucesso!\n")

def agenda_do_barbeiro():
    print("Agenda do barbeiro - Datas e Horários agendados:\n")
    if not agendamentos:
        print("Nenhum agendamento encontrado.")
    else:
        for i, agendamento in enumerate(agendamentos, 1):
            print(f"{i}. {agendamento['nome']} - {agendamento['data']} às {agendamento['horario']} | Corte: {agendamento['corte']}")
    print()

def cadastro_do_cliente():
    print("Cadastro de cliente:")
    nome = input("Qual seu nome? ")