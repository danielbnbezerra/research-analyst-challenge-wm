from bs4 import BeautifulSoup
import requests

URL= 'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos'
html_text = requests.get(URL).text

soup = BeautifulSoup(html_text, "html.parser")
general_content= soup.find_all('a')

oil_content_links = []
for content in general_content:
    link = content['href']
    if link.startswith("https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/de/ppgn/pp/"):
        oil_content_links.append(link)
