
import sys # Importando Biblioteca
import time


def valid_cpf():
    cpf = int(input("Digite o seu CPF que será ligado à conta (sem pontos ou traçoes): "))

    while cpf<10000000 or cpf>99999999999:
        cpf = int(input("\nCPF inválido, tente novamente: "))

    print("\nMuito bem, vamos seguir com o seu cadastro...\n\n")
    return cpf


def valid_idade():
    idade = (input("\nDigite agora, a sua idade neste momento: "))

    while idade.isdigit() == False:  # Restringe que o usuário apenas utilize numeros (tem que estar em str)
        idade = (input("\nNão coloque letras nem espaços neste campo: "))

    if int(idade)<18: # aqui eu reconverti 'idade' em int para fazer a operação de comparação
        print("\nPeço desculpas, mas para a criação de uma conta bancária é necessário que o cliente tenha no mínimo 18 anos")
        sys.exit() # Encerramento do código caso seja menor de idade (utilizando biblioteca importada)

    print("\nÓtimo, sua idade foi cadastrada!\n\n")
    return idade


def nome_completo():
    nome = input("\nPor Favor, digite o seu nome completo: ")

    while nome.replace(" ","").isalpha() == False: # Permite espaços, mas não numeros
        print("\nNão é permitido que tenha números neste campo!")
        nome = input("Tente novamente: ")

    print("\nMuito bem, nome cadastrado!\n")
    return nome


def sep_primeiro_nome(nome_completo):
    separar = nome_completo.split() # Separa os nomes digitados entre os espaços em arrays
    primeiro_nome = separar[0] # Selecionando o primeiro nome que está no primeiro índice do vetor
    return primeiro_nome


def cad_rua():
    rua = input("\nPor favor, insira a RUA ou AVENIDA em que você mora atualmente (sem o número de residência): ")
    return rua


def num_residencia():
    numero = int(input("\nAgora o número de sua residência: "))

    while numero <= 0:
        numero = int(input("\nO número inserido não é válido! Por favor, digite outro: "))

    return numero


def cad_cidade():
    cidade = input("\nEm que cidade você mora?\n")
    return cidade


def cad_estado():
    estado = input("Por favor, coloque as siglas do seu estado: ")

    while len(estado) != 2 or estado.isalpha() == False:  # restringi à apenas 2 caracteres e que não tenham números
        estado = input("Número de caractecteres inválido! Tente novamente: ")

    siglas = estado.upper()
    return siglas


def cad_login():
    login = input("\nHora de cadastrar seu login! Qual será seu nome de usuário?\n")
    return login


def cad_senha():
    senha_str = input("Agora preciso de uma senha de 4 dígitos pra você usar para entrar na sua conta: ")

    while len(senha_str) != 4:
        senha_str = input("Lembre-se, o número de dígitos devem ser QUATRO..: ")

    senha = int(senha_str)
    return senha

if __name__ == "__main__":
    print("\nBom Dia! Bem-Vindo(a) ao Banco Pycoin!\nPor favor, insira os seguintes dados para que possamos prosseguir com o seu cadastro! :)\n")
    decisao = 2
    while decisao == 2:
        nome_comp = nome_completo()
        idade = valid_idade()
        cpf = valid_cpf()
        rua = cad_rua()
        numero = num_residencia()
        cidade = cad_cidade()
        estado = cad_estado()
        prim_nome = sep_primeiro_nome(nome_comp)
        login = cad_login()
        senha = cad_senha()

        print(f"\n\nMuito bem {prim_nome}, preciso agora que você analise os dados cadastrados e verifique se estão corretos.\n")
        print(f"Seu nome completo é {nome_comp} e tem {idade} anos.")
        print(f"Você mora na {rua}, {numero} - {cidade} - {estado}")
        print("\nEstá tudo certo? Caso não esteja, vamos refazer o cadastro.\n1.Sim\n2.Não")
        decisao = int(input("Digite 1 ou 2 para a decisão: "))
        while decisao != 1 and decisao != 2:
            decisao = int(input("Digite APENAS 1 ou 2 para a decisão: "))
        if decisao == 2:
            print("\nTudo bem! Vamos refazer o cadastro!\n")
        else:
            print("\nExcelente! Você está cadastrado no Pycoin!\n")
        time.sleep(3)