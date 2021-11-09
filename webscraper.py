from bs4 import BeautifulSoup
import requests
import time

def find_oil_data():
    URL= 'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos'
    html_text = requests.get(URL).text

    soup = BeautifulSoup(html_text, "lxml")
    general_content= soup.find_all('a')

    oil_content_links = []
    for content in general_content:
        link = content['href']
        if link.startswith("https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/de/ppgn/pp/"):
            oil_content_links.append(link)
    
    with open(f'oil_data/oil_data.txt', 'w') as f:
        for link in oil_content_links:
            if link == oil_content_links[-1]:
                f.write(f'{link}')
            else:
                f.write(f'{link}\n')
    print ('File created')

if __name__ == '__main__':
    while True:
        find_oil_data()
        waiting_time_sec = 10
        waiting_time_min = waiting_time_sec * 60
        time.sleep(waiting_time_min * 60)
