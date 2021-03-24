"""
Data Mining com Python
Aula 03 - 23/03/2021
Parte 3/
"""
import requests
from requests.auth import HTTPBasicAuth


def example1():
    """Exemplo 1 de acesso a uma API protegida."""
    username = "email@company.com"
    token = "abcdefgh"
    url = "https://www.google.com"

    params = {"maxResults": 100}

    req = requests.request(
        "GET",
        url,
        headers={"Accept": "application/json"},
        params=params,
        auth=HTTPBasicAuth(username, token)
    )

    return req.json()


def example2():
    """Exemplo 2 de acesso a uma API protegida."""
    token = "abcdefgh"
    url = "https://www.google.com"

    params = {"maxResults": 100}

    req = requests.request(
        "GET",
        url,
        headers={
            "Accept": "application/json",
            "Authorization": "Bearer " + token
        },
        params=params,
    )

    return req.json()
