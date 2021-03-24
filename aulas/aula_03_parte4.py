"""
Data Mining com Python
Aula 03 - 23/03/2021
Parte 4/

- Criar uma conta em https://developer.nytimes.com/accounts/create
- Entrar em https://developer.nytimes.com e fazer login
"""
from pprint import pprint

import requests


APIKEY = "EnwweSZDhmlf7wCnzfYcRoqsrAW0JGQ6"


def nytimes_article(query):
    """Extrai artigos do NYTimes de acordo com uma pesquisa."""
    begin_date = "20210223"
    filter_query = "\"glocations: (\"BRAZIL\")\""
    page = "0"
    sort = "relevance"
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

    params = {
        "q": query,
        "api-key": APIKEY,
        "begin_date": begin_date,
        "fq": filter_query,
        "page": page,
        "sort": sort
    }

    req = requests.request(
        "GET",
        url,
        params=params
    )

    return req.json()


def nytimes_topstories(section):
    """Extrai dados das principais notícias do NYTimes."""
    url = f"https://api.nytimes.com/svc/topstories/v2/{section}.json"
    params = {"api-key": APIKEY}

    req = requests.request(
        "GET",
        url,
        params=params
    )

    return req.json()

pprint(nytimes_topstories("science"))
# pprint(nytimes_article("science"))
