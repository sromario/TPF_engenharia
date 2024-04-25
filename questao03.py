
# def para achar os maiores valores
def repeticoes(tamanhos):
    repeticao_maior = 0
    atual = 1

    # percorrer tamanhos e comaprar valores
    for i in range(1, len(tamanhos)):
        if tamanhos[i] == tamanhos[i - 1]:
            atual += 1
        else:
            maior_repeticao = max(repeticao_maior,atual)
            atual = 1

    # Verifica a sequência é a maior
    repeticao_maior = max(repeticao_maior, atual)

    return repeticao_maior

# Ler a entrada do arquivo
with open('questao03.txt', 'r') as arquivo:
    total = int(arquivo.readline().strip())
    tamanhos = arquivo.readline().strip().split()

# chamar def para maior seqeuncia de repetições
resultado = repeticoes(tamanhos)


# exibir valores
print('ENTRADA')
print(total)
print(" ".join(map(str, tamanhos)))


# Exiba o resultado
print('SAÍDA')
print(f'{resultado} medições de {tamanhos[0]}')
