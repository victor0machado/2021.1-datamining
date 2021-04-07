"""
Data Mining com Python
06/04/2021

ETL
    - Extração
    - Transformação
    - Carregamento

PROTOTIPAGEM

Jupyter Notebook
- Sucessor do IPython Notebook, publicado inicialmente em 2010
- Consegue usar várias linguagens dom Jupyter (R e Java)
- Grande aplicação em DS e DM
- É open source

Vantagens:
- Rápida prototipagem e edição dos dados extraídos
- Execução simples em blocos
- Fácil de gerar relatórios
- Ambiente isolado, favorece o trabalho em servidores

Desvantagens:
- Muito difícil de versionar código
- Fraca integração com IDEs, dificultando correção de estilo e linting
- Muito difícil de testar
- Não-linearidade do código
- Ruim para lidar com grandes tarefas assíncronas

Exercício inicial:
- Extrair todos os arquivos .csv de https://github.com/cmusam/fortune500
- Salvar tudo em um único arquivo na pasta ".\dados\"
"""
import csv

import requests


MAIN_URL = "https://raw.githubusercontent.com/cmusam/fortune500/master/csv/fortune500-"
CSV_PATH = "dados\\fortune500.csv"


def collect_year_data(year, fortune_data):
    """Extract yearly data."""
    print(f"Collecting data from {year}...")
    url = f"{MAIN_URL}{year}.csv"

    req = requests.get(url)
    raw_data = req.text.split("\n")[1:]
    raw_data = [data.replace("\r", "") for data in raw_data]

    if raw_data[-1] == "":
        raw_data = raw_data[:-1]

    print(len(raw_data))
    fortune_data.extend([f"{year},{data}" for data in raw_data])


def save_to_csv(data):
    """Save list to .csv."""
    print("Saving file...")

    data = ["year,rank,company,revenue ($ millions),profit ($ millions)"] + data
    data = [row.replace(", ", "; ").replace("\"", "") for row in data]  # list comprehension

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=",")
        for row in data:
            spamwriter.writerow(row.split(","))


def main():
    """Application entry point."""
    fortune_data = []
    for year in range(1955, 2020):
        collect_year_data(year, fortune_data)

    save_to_csv(fortune_data)
    print("Done.")


if __name__ == "__main__":
    main()
