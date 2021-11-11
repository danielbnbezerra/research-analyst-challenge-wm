from bs4 import BeautifulSoup
import requests
import time
import os

def find_oil_data():
    URL= 'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos'
    OIL_DATA_LOCATION = 'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/de/ppgn/pp/'
    
    html_text = requests.get(URL).text

    soup = BeautifulSoup(html_text, "lxml")
    general_content= soup.find_all('a')

    oil_content_links = ['']
    for content in general_content:
        link = content['href']
        if link.startswith(OIL_DATA_LOCATION):
            oil_content_links.append(link)
    
    for link in oil_content_links:
        file_name = link
        if OIL_DATA_LOCATION in file_name:
            file_name = link.replace(OIL_DATA_LOCATION,'')
            with open(f'oil_data/{file_name}', 'wb') as f:
                response = requests.get(link)
                f.write(response.content)
            os.system(f'unzip -o oil_data/{file_name} -d oil_data/{file_name[0:-4]}')
            os.system(f'rm oil_data/{file_name}')

    print('Folders Created Successfully')

#This was used to automatize the proccess but it could be made through cron, a task manager for linux, so we could schedule the script to rerun.
#In my opinion it would be a more sofisticate resolution but I made it this way to be shown in code.
if __name__ == '__main__':
    while True:
        find_oil_data()
        #Program will rerun after 30s
        waiting_time_hour = 1 * 60 * 60
        time.sleep(waiting_time_hour)