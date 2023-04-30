# Project_Spark

## Dependencies

```bash
pip install pyspark
```

## Descrição

- Projeto exemplo de utilização do Spark para processamento de dados. O projeto consiste em um script que lê um arquivo CSV, faz o processamento dos dados e salva o resultado em um arquivo CSV.

- O script foi desenvolvido utilizando a linguagem Python.

- Foi utilizado o databricks para desenvolvimento do projeto.

- O notebook do projeto do databricks esta disponível no diretório do projeto.

## Como foi feito

- Foi criado uma conta no databricks para desenvolvimento do projeto.

- Foi Intanciado um cluster no databricks para execução do projeto.

- Foi criado um notebook no databricks

- Utilizando o dataframe do proprio databricks foi feito a leitura do arquivo CSV.

- Foi feito todo processamento dos dados utilizando o dataframe do databricks com spark.

## MongoDB

### Instalação

- pip install pymongo

### Conexão

- from pymongo import MongoClient

- client = MongoClient("String de conexão")

- db = client["nome do banco"]

- collection = db["nome da coleção"]
