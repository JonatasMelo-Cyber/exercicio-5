#Exercicio 5
#1 precisa ter agendamento
#2 precisa ter cadastro de agenda do barbeiro
#3 precisa ter cadastro do serviço ex: corte simples com preço
#4 precisa ter cadastro do cliente(nome, telefone, email)
#5 precisa ter escolha de barbeiro
#6 reagendamento rapido
#7 controle de fatura de barbeiro
#8 historico de cliente
#9 feedback de cliente
def agendar_servico():
    print("Seja Bem vindo!")
    nome = input("Qual seu nome? ")
    telefone = input("Qual seu telefone? ")
    data = input("Marcar data: ")
    corte = input("Personalize seu corte: ")
    horario = input("Marcar horario: ")
    
agendar_servico()

def agenda_do_barbeiro():
    print("Datas e Horarios, Disponiveis.")
agenda_do_barbeiro()

def cadastro_do_cliente():
    print("Cadrastrar cliente.")
    nome = input("Qual seu nome? ")
    telefone = input("Qual seu telefone para contato? ")
    email = input("Digite seu email de verificação: ")
cadastro_do_cliente()
