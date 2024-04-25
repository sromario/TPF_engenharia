import requests

# CEP
cep = '79074290' #escolher cep para consultar individual

# ViaCep
url = f'https://viacep.com.br/ws/{cep}/json/'
resposta = requests.get(url)


if resposta.status_code == 200:
    # Exibir os dados do endereço
    endereco = resposta.json()
    print(endereco)
else:
    print(f"Erro ao consultar o CEP {cep}: {resposta.status_code}")
