#   def para achar valor perdido
def fiscal(total_fiscais,fiscais_completa,fiscais_incompleta):
    somaLista1 = 0
    somaLista2 = 0
    for i in fiscais_incompleta:
        somaLista1= somaLista1+i
        continue
     
    for i in fiscais_completa:
        somaLista2 = somaLista2+i
        continue
    
    print('SAIDA')
    print(somaLista2 - somaLista1) 


# executar
if __name__== "__main__":
    print('ENTRADA')

    # abrir arquivo.txt
    with open ('questao02.txt', 'r') as arquivo:
        exemplo = 1

        for linha in arquivo:
        # ler primeira linha do total de fiscais
         if linha.strip():
            # Imprimir número do exemplo
            print(f"Exemplo {exemplo}:")
            exemplo += 1

            # Ler o número de fiscais
            total_fiscais = int(linha.strip())

            # Ler a lista de fiscais incompletos
            fiscais_incompleta = list(map(int, arquivo.readline().strip().split()))

            # Criar a lista de fiscais completa
            fiscais_completa = list(range(1, total_fiscais + 1))

            # Imprimir total de fiscais
            print(total_fiscais)

            # Imprimir lista de fiscais incompletos em uma linha
            print(" ".join(map(str, fiscais_incompleta)))

             # chamar def para achar valor perdido
            fiscal(total_fiscais,fiscais_completa,fiscais_incompleta)

       