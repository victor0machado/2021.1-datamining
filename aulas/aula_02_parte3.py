"""
Data Mining com Python
Aula 02 - 09/03/2021
Parte 3/3
"""

# Dicionários
alunos = [
    {
        "nome": "Iago",
        "nota": 7.5,
        "cpf": "111",
        "curso": "EGP"
    },
    {
        "nome": "Rachel",
        "nota": 7,
        "cpf": "222",
        "curso": "ECO"
    },
    {
        "nome": "Vitor",
        "nota": 8,
        "cpf": "333",
        "curso": "EGC"
    }
]

for aluno in alunos:
    print(aluno)


TEXTO = "O rato roeu a roupa do rei de Roma"
print(len(TEXTO))
print(TEXTO[4])
print(TEXTO[:10])
print("Rato" in TEXTO)

for letra in TEXTO:
    print(letra)

print(TEXTO.count("r"))
print(TEXTO.count("R"))

print(TEXTO.find("Roeu"))
# print(TEXTO.index("Roeu")) -> vai subir exceção do tipo ValueError

palavras = TEXTO.split(" ")
print(palavras)

print(" ".join(palavras))

print(TEXTO.upper())
print(TEXTO.lower())
print(TEXTO.capitalize())
print(TEXTO.title())

print("A".isupper())
print("A".islower())
print("Rato roeu".istitle())
print("A".isalnum())
print("?".isalpha())
print("?".isdigit())
print(" ".isspace())

print("Oi".ljust(20), "-")
print("Oi".rjust(20), "-")
print("Oi".center(20), "-")

print("     Olá     ".lstrip(), "-")
print("     Olá     ".rstrip(), "-")
print("     Olá     ".strip(), "-")

print("O rato roeu".startswith("O "))
print("O rato roeu".endswith("O "))

print(TEXTO.replace("rato", "gato"))


# f-strings
# formatted strings
print("O TEXTO inserido foi:", TEXTO, "!")
print(f"O TEXTO inserido foi: {TEXTO}!")


PRECO = 14.0
print(f"Valor: R${PRECO:8.2f}")
