import requests
import jsonpath

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')
#
# print(resultados)

# primeiro resultado da lista
# primeira = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
# print(primeira)

# nome do primeiro elemento
# nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
# print(nome)

# acessar email
# email = jsonpath.jsonpath(avaliacoes.json(), 'results[0].email')
# print(email)

# acessar nota data
# nota_data = jsonpath.jsonpath(avaliacoes.json(), 'results[0].avaliacao')
# print(nota_data)

#curso id
# curso_id = jsonpath.jsonpath(avaliacoes.json(), 'results[0].curso')
# print(curso_id)

# Todos os nomes das pessoas que avaliaram o curso
# nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nomes')
# print(nomes)