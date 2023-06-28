import time
import criarCB # Importando o arquivo Python

def menu_principal():
    escolha = int(input("Escolha uma das seguintes opções de operação do nosso banco:\n1.Cadastro\n2.Saque\n3.Depósito\n"))
    while escolha < 1 or escolha > 4:
        escolha = int(input("O número digitado não é uma escolha válida. Tente novamente:\n1.Cadastro\n2.Saque\n3.Depósito\n"))
    return escolha

def login():
    log = input("\nDigite seu nome de usuário para o login: ")
    while log != criarCB.login:
        print("Opa, acredito que este nome de usuário não esteja cadastrado!")
        log = input("\nDigite seu nome de usuário para o login: ")
    return log

def senha_op():
    sen = int(input("Agora digite a senha correspondente a este login: "))
    while sen != criarCB.senha:
        sen = int(input("A senha está incorreta. Tente novamente: "))
    return sen


def extrato(atualizar):
    time.sleep(1)
    quantidade_atual = 1000 + int(atualizar)
    print(f"\nVocê está com um total de {quantidade_atual}!\n")
    return quantidade_atual


def saque(quantidade_atual):
    time.sleep(2)
    print("\nOlá, você está no ambiente de saque do Pycoin!")
    sacar = int(input("Quantos reais você deseja sacar? "))
    if sacar > quantidade_atual:
        print("\nNão foi possível concluir a operação, você tentou sacar mais do que o extrato permite\n")
    elif sacar < 0:
        print("\nNão é válido o saque de números negativos...\n")
    else:
        print(f"\nMuito bem! {sacar} reais retirado com sucesso!\n")
        quantidade_atual = quantidade_atual - sacar
        print(f"Agora seu extrato está com {quantidade_atual} reais\n")
        return quantidade_atual


def deposito(quantidade_atual):
    time.sleep(2)
    print("\nOlá, você está no ambiente de depósito do Pycoin!")
    depositar = int(input("Quantos reais você deseja depositar? "))
    if depositar < 0:
        print("\nNão é válido o depósito de números negativos\n")
    else:
        print(f"\nMuito bem! {depositar} reais já foram adicionados na sua conta!\n")
        quantidade_atual = quantidade_atual - depositar
        print(f"Agora seu extrato está com {quantidade_atual} reais\n")
        return quantidade_atual

atualizar = 0
decisao = 1
print("\nBem-Vindo(a) ao menu do Banco Pycoin!\n")

while decisao == 1:
    menu = menu_principal()
    if menu == 1:
        exec(open('criarCB.py').read())
    elif menu == 2:
        quantidade = extrato(atualizar)
        atualizar = (saque(quantidade)*(-1))

    elif menu == 3:
        quantidade = extrato(atualizar)
        atualizar = deposito(quantidade)
    else:
        print("\nEsta opção não está disponível!\n")
    decisao = int(input("Deseja fazer mais alguma ação no Pycoin?\n1.Sim\n2.Não\n-> "))
    if decisao == 1:
        print("Muito bem, vamos lá\n")
        time.sleep(2)
    elif decisao == 2:
        print("Tudo bem! Pycoin agradece a visita! :)")