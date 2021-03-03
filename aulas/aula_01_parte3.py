"""
Data Mining com Python
Aula 01 - 02/03/2021
Parte 3/3
"""

def e_par(num):
    """Retorna True caso num seja par."""
    if num % 2 == 0:
        return True
    else:
        return False


def e_par_melhorada(num):
    return num % 2 == 0


print(e_par(7))
print(e_par_melhorada(8))
print(e_par_melhorada(9))


def calcula_conceito(nota):
    if nota > 9:
        return "A"
    elif nota > 8:
        return "B"
    elif nota >= 7:
        return "C"
    else:
        return "F"


def le_dado():
    dado = input("Escreva alguma coisa: ")

    if dado == "":
        print("Você não escreveu nada!")
        return "ERRO!!!!"

    return dado


print(le_dado())
