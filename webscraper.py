from bs4 import BeautifulSoup
import requests

URL= 'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos'

html_text = requests.get(URL).text
soup = BeautifulSoup(html_text, "html.parser")
#oil_content = soup.select("li div ul ul ul")
#print(oil_content)
general_content = soup.find_all(name="a", class_="internal-link", attrs= 'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/de/ppgn/pp/')
#print (general_content)
general_content_texts = []
general_content_links = []
for content in general_content:
    #text = content.getText()
    #general_content_texts.append(text)
    link = content.get("href")
    general_content_links.append(link)
print (general_content_links)
#print(general_content_texts)