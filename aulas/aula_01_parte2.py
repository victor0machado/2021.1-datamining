def escreve_linha_cabecalho(separador, tam):
    print(separador * tam)


def escreve_cabecalho(titulo, separador="=", tam=50):
    escreve_linha_cabecalho(separador, tam)
    print(titulo)
    escreve_linha_cabecalho(separador, tam)


escreve_cabecalho("Exemplo")
escreve_cabecalho("Exemplo 2", separador="-")
escreve_cabecalho("Exemplo 3", separador="-", tam=40)
escreve_cabecalho("Exemplo 4", tam=40)
escreve_cabecalho("Exemplo 5", tam=40, separador="*")
escreve_cabecalho("Exemplo 6", "*", 40)


def soma_dois_numeros(num1, num2):
    return num1 + num2


print(soma_dois_numeros(4, 8))


def celsius_para_fahrenheit(temp_celsius):
    return (temp_celsius * 9) / 5 + 32


print(celsius_para_fahrenheit(0))
