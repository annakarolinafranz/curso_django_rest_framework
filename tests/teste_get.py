import requests

headers = {'AUthorization': 'Token 099cd66b13f62cb698873b7c7442c4ab821a2823'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

# print(resultado.json())

# print(resultado.status_code)  # error 404

# Testando se o endpoint está correto
assert resultado.status_code == 200

# Testando a quatidade de registros
assert resultado.json()['count'] == 2

# Testando se o titulo do primeiro curso está correto
assert resultado.json()['results'] == 'Criação de APIs REST com Djando REST Framework'

