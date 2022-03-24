import requests #biblioteca de requisição
import json #Biblioteca com o formato de compartilhamento de dados entre site

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL") # Linha de acesso a API
cotacoes = cotacoes.json() # Formatação dos dados
cotacao_dolar = cotacoes['USDBRL']["bid"]

#print(cotacoes)
print(cotacao_dolar)