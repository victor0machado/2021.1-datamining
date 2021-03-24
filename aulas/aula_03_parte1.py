"""
Data Mining com Python
Aula 03 - 23/03/2021
Parte 1/

Processo de Tratamento de Dados (ETL):
- Extração
- Transformação
- Carregamento

Extração de dados:
- Dados locais;
- Dados em um servidor;
- Dados na web.

Formatos mais comuns:
- .txt;
- .csv; # comma-separated values
- .json;
- .html;
- .xml.

módulos
biblioteca

HTTP:
- GET (solicita informações)
- POST (enviar informações)

- Códigos de satus:
    - 2XX (sucesso - 200);
    - 4XX - erro do cliente:
        - 400 - Requisição inválida
        - 401 - Não autorizado
        - 403 - Proibido
        - 404 - Não encontrado
    - 5XX - outros erros:
        - 500 - Erro interno do servidor
        - 503 - Serviço indisponível
        - 504 - Gateway timeout
"""
import math
from math import ceil, floor
from math import *
from math import factorial as fact
import json
from pprint import pprint

import requests


print(math.factorial(5))

print(ceil(4.9))
print(floor(4.9))

print(fact(7))

print(fabs(-5.5))


# Pegando dados da SWAPI

req = requests.get("https://swapi.dev/api/people/")
print(req)
print(req.text)
print(req.headers)
print(req.json())
print(req.status_code)


with open("sw.json", "w") as arquivo:
    json.dump(req.json(), arquivo, indent=4)

with open("sw.json", "r") as arquivo:
    conteudo = json.load(arquivo)

print(conteudo)

url = req.json()["next"]
print(url)
pprint(req.json()["results"], indent=4)
