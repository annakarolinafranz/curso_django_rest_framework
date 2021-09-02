import requests

# GET Avaliações
# avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# Acessando o código de status HTTP
# print(avaliacoes.status_code)

# Acessando os dados da resposta
# print(avaliacoes.json())
# print(type(avaliacoes.json()))

# Acessando a quantidade de registros
# print(avaliacoes.json()['count'])

# Acessando a proxima pagina de resultados
# print(avaliacoes.json()['next'])

# Acessando os resultados dessa página
# print(avaliacoes.json()['results'])  # lista de resultado
# print(type(avaliacoes.json()['results']))

# Acessando o primeiro elemento da lista de resultados
# print(avaliacoes.json()['results'][0])

# Acessando o ultimo elemento da lista de resultados
# print(avaliacoes.json()['results'][-1])

# Acessando somente o nome da pessoa que fez a ultima avaliação
# print(avaliacoes.json()['results'][-1]['nome'])

# GET Avaliacao
# avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/7/')
#
# print(avaliacao.json())
