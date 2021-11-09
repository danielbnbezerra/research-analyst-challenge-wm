from bs4 import BeautifulSoup
import requests
import time

def find_oil_data():
    URL= 'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos'
    html_text = requests.get(URL).text

    soup = BeautifulSoup(html_text, "html.parser")
    general_content= soup.find_all('a')

    oil_content_links = []
    for content in general_content:
        link = content['href']
        if link.startswith("https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/de/ppgn/pp/"):
            oil_content_links.append(link)

if __name__ == '__main__':
    while True:
        find_oil_data()
        waiting_time_sec = 10
        waiting_time_min = waiting_time_sec * 60
        time.sleep(waiting_time_min * 60)
