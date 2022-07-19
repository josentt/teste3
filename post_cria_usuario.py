import requests
from pprint import pprint
_print = print
#print = pprint

url = 'http://127.0.0.1:3001/users'

users_data = {
    "nome": "nome válido",
    "password": "senha válida",
    "email": "email_valido@email.com"
}

response = requests.post(url=url, json=users_data)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print('Status Code', response.status_code)
    print('Reason', response.reason)
    print('Text', response.text)
    print('JSON', response.json())
    #print('Byte', response.content)
else:
    # Erros
    print('Status Code', response.status_code)
    print('Reason', response.reason)
    print('Text', response.text)
    #print('Byte', response.content)
