import math

def jump_search(lista, valor):
    try:
        n = len(lista)
        passo = int(math.sqrt(n))
        anterior = 0
        numeros_passados = []

        while passo < n:
            if lista[passo] >= valor:
                break
            anterior = passo
            numeros_passados.append(lista[anterior])
            passo += int(math.sqrt(n))

        # Busca linear no bloco anterior
        while anterior < passo and anterior < n:
            if lista[anterior] == valor:
                return True
            anterior += 1
            numeros_passados.append(lista[anterior])

        print(f"Números passados pelo algoritmo: {numeros_passados}")
        return False
    except ValueError as e:
        print(f"Erro: {e}")
        return False

def main():
    # Lista para armazenar os números
    numeros = []

    # Loop para adicionar números à lista
    numero = -1
    while numero != 0:
        try:
            numero = int(input("Digite um número (0 para sair): "))
            if numero != 0:
                numeros.append(numero)
        except ValueError:
            print("Erro: Valor inválido digitado.")

    # Ordenar a lista
    numeros.sort()

    # Solicitar o valor a ser buscado
    valor_busca = int(input("Digite o valor a ser buscado: "))

    # Realizar a busca utilizando o Jump Search
    encontrado = jump_search(numeros, valor_busca)

    # Exibir o resultado da busca
    if encontrado:
        print(f"O valor {valor_busca} foi encontrado na lista!")
    else:
        print(f"O valor {valor_busca} não foi encontrado na lista.")

if __name__ == "__main__":
    main()
