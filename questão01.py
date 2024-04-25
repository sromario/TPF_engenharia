import csv
import requests
import json

def lerArquivo_csv(csv_arquivo):
    ceps = []
    with open(csv_arquivo, 'r', newline='') as arquivo_csv:
        ler_csv = csv.reader(arquivo_csv)
        for linha in ler_csv:
            for cep in linha:
                cep_formatado = cep.strip()  # Remover espaços em branco antes e depois do CEP
                ceps.append(cep_formatado)
    return ceps


# exibir ceps
ceps = lerArquivo_csv('questao01.csv')
print(ceps)

# consultar ViaCep e adicionar dados
enderecos = []
for cep in ceps:
    if cep.strip():  # Verificar se o CEP não está vazio
        # Consultar ViaCep
        url = f'https://viacep.com.br/ws/{cep}/json/'
        resposta = requests.get(url)
        
        # Verificar se a resposta foi bem-sucedida
        if 200 <= resposta.status_code < 300:
            try:
                endereco = resposta.json()
                
                # Processar os dados do endereço
                logradouro = endereco.get('logradouro', 'Indisponível')
                bairro = endereco.get('bairro', 'Indisponível')
                cidade = endereco.get('localidade', 'Indisponível')
                estado = endereco.get('uf', 'Indisponível')
                
                # Adicionar dados processados à lista de endereços
                enderecos.append([cep, logradouro, bairro, cidade, estado])
                
                # Substituir valores ausentes por 'Indisponível'
                for i in range(len(enderecos[-1])):
                    if not enderecos[-1][i]:
                        enderecos[-1][i] = 'Indisponível'
            except json.decoder.JSONDecodeError:
                print(f'Erro ao decodificar JSON para o CEP {cep}')
        


# escrever os dados em um novo csv
def escrever_csv(enderecos, novo_csv):
    with open(novo_csv, 'w', newline='') as arquivo_csv:
        csv_writer = csv.writer(arquivo_csv)
        csv_writer.writerow(['CEP', 'Logradouro', 'Bairro', 'Cidade', 'Estado'])
        for endereco in enderecos:
            csv_writer.writerow(endereco)


# Substituir valores ausentes por 'Indisponível'
    for endereco in enderecos:
        for i in range(len(endereco)):
            if not endereco[i]:
                endereco[i] = 'Indisponível'


escrever_csv(enderecos, 'enderecos_completo.csv')
