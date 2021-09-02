import requests

headers = {'AUthorization': 'Token 099cd66b13f62cb698873b7c7442c4ab821a2823'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo": "Novo Curso de Scrum 3",
    "url": "http://www.geekuniversity.com.br/ncs3"
}

# Buscando o curso com ID 6
# curso = requests.get(url=f'{url_base_cursos}6/', headers=headers)
#
# print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}6/', headers=headers, data=curso_atualizado)  # conceito f string

# Testando o código de status HTTP
assert resultado.status_code == 200

# Testando o titulo
assert resultado.json()['tituo'] == curso_atualizado['titulo']