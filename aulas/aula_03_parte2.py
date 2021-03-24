"""
Data Mining com Python
Aula 03 - 23/03/2021
Parte 2/
"""
import sys
import json
from dataclasses import dataclass

import requests


MAIN_URL = "https://swapi.dev/api/people/"
HTTP_SUCCESS = 200
MAX_RETRIES = 5


@dataclass
class Error():
    """Códigos de erro."""
    max_retries_reached = -1


def main():
    """Ponto de entrada da aplicação."""
    print(f"Coletando dados de {MAIN_URL}...")
    url = MAIN_URL
    full_data = []
    num_retries = 0

    while True:
        req = requests.get(url)

        if req.status_code == HTTP_SUCCESS:
            data = req.json()

            full_data.extend(data.get("results"))

            if data.get("next") is None:
                break

            url = data["next"]
            num_retries = 0
        elif num_retries <= MAX_RETRIES:
            num_retries += 1
        else:
            print("Número máximo de tentativas atingido!")
            print(f"Erro mais recente: {req.status_code}.")
            sys.exit(Error.max_retries_reached)

    with open("people.json", "w") as resource:
        json.dump(full_data, resource, indent=4)

    print(f"Dados de {MAIN_URL} coletados com sucesso!")
    print(f"Coletadas {len(full_data)} entradas.")


if __name__ == "__main__":
    main()
