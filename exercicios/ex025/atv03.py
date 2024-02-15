import math

def jump_search(lista, valor):
  """
  Realiza a busca por um valor em uma lista ordenada utilizando o algoritmo Jump Search.

  Parâmetros:
    lista: A lista ordenada onde a busca será realizada.
    valor: O valor a ser buscado na lista.

  Retorno:
    True se o valor for encontrado na lista, False caso contrário.
  """

  try:
    n = len(lista)
    passo = int(math.sqrt(n))
    anterior = 0
    numeros_percorridos = []

    while passo < n:
      if lista[passo] >= valor:
        break
      anterior = passo
      passo += passo
      print(f"Número percorrido: {lista[anterior]}")

    # Busca linear no bloco anterior
    while anterior < passo and anterior < n:
      if lista[anterior] == valor:
        return True
      anterior += 1
      numeros_percorridos.append(lista[anterior])
      print(f"Número percorrido: {lista[anterior]}")

    print(f"Números percorridos: {numeros_percorridos}")
    return False
  except ValueError:
    print("Erro: Valor inválido digitado.")
    return False

def main():
  # Lista para armazenar os números
  numeros = []

  # Loop para adicionar números à lista
  numero = -1
  while numero != 0:
    try:
      numero = int(input("Digite um número (0 para sair): "))
    except ValueError:
      print("Erro: Valor inválido digitado.")
    if numero != 0:
      numeros.append(numero)

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
