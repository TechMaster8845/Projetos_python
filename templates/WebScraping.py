'''
Template
Útil para: Coletar informações de sites automaticamente
'''
import requests
from bs4 import BeautifulSoup

def coletar_dados(url):
    resposta = requests.get(url)
    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, "html.parser")
        return soup.title.text  # Pega o título da página
    else:
        return "Erro ao acessar o site."

def main():
    url = "https://www.python.org/"
    print(f"Título da página: {coletar_dados(url)}")

if __name__ == "__main__":
    main()

