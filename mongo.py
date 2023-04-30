import os
from pymongo import MongoClient
import csv
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

string_connection = os.getenv("STRING_CONNECTION")

df = pd.read_csv('./casos_leves_covid_2022_recife.csv')

print(df.head())


# crie um cliente MongoDB
client = MongoClient(string_connection)

# acesse um banco de dados e uma coleção
db = client["data_covid"]
collection = db["doenca"]


# with open('./casos_leves_covid_2022_recife.csv', 'r') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for i, row in enumerate(reader):
#         if i >= 100:  # Verifica se já foram lidas 100 linhas
#             break
#         # Insere o documento no banco de dados
#         row = {str(key): value for key, value in row.items()}
#         collection.insert_one(row)

# collection.insert_many(data)
