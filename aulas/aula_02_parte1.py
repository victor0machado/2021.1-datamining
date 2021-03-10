"""
Data Mining com Python
Aula 02 - 09/03/2021
Parte 1/3
"""

# Estruturas de repetição
def le_nome():
    """Ler o nome passado pelo usuário, e imprime na tela."""
    nome = ""
    while nome == "":
        nome = input("Informe o seu nome: ")
        if nome == "":
            print("Você não informou nada! Tente novamente!")

    print("Olá,", nome)


def contagem_regressiva(numero):
    """Imprime de numero até 0, ou avisa que o valor é inválido, caso numero
    seja menor que 0."""
    if numero < 0:
        print("Valor inválido!")

    while numero >= 0:
        print(numero)
        numero -= 1


def seleciona_opcao():
    """Aguarda o usuário selecionar uma opção e volta para o menu."""
    while True: # loop infinito
        opcao = input("Digite 1, 2 ou 3, ou aperte ENTER para encerrar. ")
        if opcao == "":
            break

    print("Finalizando o programa...")


def le_nomes_turma(tamanho_turma):
    """Lê os nomes de todos os integrantes da turma."""
    for indice in range(1, tamanho_turma + 1):
        nome = input("Informe o nome do aluno na posição " + str(indice) + ":")
        print(nome)


def imprime_num_pares(valor_limite):
    """Imprime todos os números pares, de 0 até o valor_limite."""
    for numero in range(0, valor_limite + 1, 2):
        print(numero)


def contagem_regressiva_alt(inicio):
    """Faz a contagem regressiva com for."""
    for numero in range(inicio, -1, -1):
        print(numero)
