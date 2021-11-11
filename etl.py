import pandas as pd
import os

base = '/home/delian/Área de trabalho/Cursos/desafio-wood-mackenzie/modulo-git/oil_data'
folders = os.listdir(base)

df_total_sea = pd.DataFrame()
df_total_land = pd.DataFrame()
df_total_pre_salt = pd.DataFrame()

for subdir, dirs, folders in os.walk(base):
    for folder in folders:
        with open(folder, 'r') as f:
            f.
            for file in files:
                if file.endswith('.xlsx'):
                    excel_file_sea = pd.ExcelFile(file)
                    df_total_sea = df_total_sea.append(excel_file_sea)
                    df_total_sea.head(5)
                
