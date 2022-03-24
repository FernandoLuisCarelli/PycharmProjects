import requests
import json

cep = int(input('Digite o CEP :'))
#cep1 = "https://cep.awesomeapi.com.br/json/" + str(cep)
buscaCep = requests.get("https://cep.awesomeapi.com.br/json/" + str(cep))
buscaCep = buscaCep.json()
#format_cep = buscaCep['CEP']

#print(format_cep)
print(buscaCep)