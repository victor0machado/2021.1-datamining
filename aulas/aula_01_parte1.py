# Tipos de dados

# inteiro - int
x = 10

# número com casa decimal - float
y = 4.5

# textos - strings
z = "oi"

# booleanos - verdadeiro ou falso
w = True
k = False

# entendendo algoritmos

# entrada de dados
# processamento
# saída de dados

# funções

print("olá, mundo")

# variáveis

morador_novo = "Victor"

print("olá, ", morador_novo, "!", sep="")
print("olá, " + morador_novo)

dia = 2

print("Hoje é dia", dia)

# nome = input("Informe o seu nome: ")
# print("olá,", nome)

# Leia dois números e mostre a soma desses números

# num1 = int(input("Informe um número: "))
# num2 = float(input("Informe outro número: "))
# print(str(num1 + num2))

# Operações numéricas

x = 2
y = 10
z = -4.582

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y) # divisão inteira
print(x % y) # operador módulo - resto da divisão
print(x ** y) # exponenciação
print(abs(z))
print(int(z))
print(float(x))
print(round(z, 1))

# Precedência dos operadores

"""
**

*, /, //, %

+, -
"""

print(x * (2 + y) ** 2)

# Operadores com strings

print("olá, " + "Victor")
print("=" * 15)

# Operações booleanas

x = True
y = False

print(x and y)
print(x or y)
print(not x)

# Operadores de comparação

x = 2
y = 10

print("-" * 15)
print(x < y)
print(x <= y)
print(x > y)
print(x >= y)
print(x == y)
print(x != y)
print(x is y)
print(x is not y)

print((x == 2 or x < y) and (x + 3 <= 2))
