"""
Data Mining com Python
Aula 02 - 09/03/2021
Parte 2/3
"""

# Listas
aprovados = ["Iago", "Rachel", "Vitor", "Ercilio", "Catharina", "Diogo", "Pedro", "Renan", "Luiz"]
num_premiados = 3

print("A lista:", aprovados)
print("Primeiro colocado:", aprovados[0])

print("Primeira pessoa não premiada:", aprovados[num_premiados])
print("Total de aprovados:", len(aprovados))

if "Victor" in aprovados:
    print("Parabéns, você foi aprovado!")
else:
    print("Que pena!")

premiados = aprovados[:num_premiados]
print("Premiados:", premiados)

aprovados_nao_premiados = aprovados[num_premiados:]
print("Aprovados e não premiados:", aprovados_nao_premiados)

print("Último premiado:", premiados[-1])

print("Alunos em posições pares:", aprovados[1::2])

aprovados[2] = "Renan"
if "Renan" in aprovados:
    print("Foi aprovado!")
else:
    print("Não foi aprovado!")

print(aprovados)

aprovados.append("Vitor")
print(aprovados)

aprovados.insert(5, "Leonardo")
print(aprovados)

aprovados.remove("Diogo")
print(aprovados)

if "Victor" in aprovados:
    aprovados.remove("Victor")

nome = aprovados.pop()
print(aprovados)
print(nome)

aprovados.pop(7)
print(aprovados)

novos_aprovados = ["Vitor", "Diogo"]
aprovados.extend(novos_aprovados)
print(aprovados)

for aluno in aprovados:
    print(aluno)

for cont in range(len(aprovados)):
    print(aprovados[cont])

for pos, nome in enumerate(aprovados):
    print(pos + 1, "-", nome)

lista = [1, 1.5, "texto", True, [1, 2, 3], {1: "exemplo"}]

notas = [4, 8, 4.5, 6.8, 2.55, 9.7, 6.6]
print("Menor valor:", min(notas))
print("Menor valor:", max(notas))
print("Média:", sum(notas) / len(notas))

notas.sort()
print(notas)

notas.reverse()
print("Notas em ordem decrescente:", notas)

notas.append(4.5)
print("Número de pessoas que tiraram 4.5:", notas.count(4.5))
