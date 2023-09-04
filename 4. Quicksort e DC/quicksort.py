# Minha solução prévia, com base na explicação teórica
def myquicksort(lista):
    # caso Base
    if len(lista) < 2:
        return lista

    # caso recursivo
    pivo = lista[0]
    maiores = []
    menores = []

    for n in lista:
        if pivo == n: continue
        maiores.append(n) if n >= pivo else menores.append(n)

    return quicksort(menores) + [pivo] + quicksort(maiores)

def quicksort(array):
  # caso base
  if len(array) < 2:
    return array
  # caso recursivo
  else:
    pivo = array[0]
    menores = [i for i in array[1:] if i <= pivo]
    maiores = [i for i in array[1:] if i > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)

lista = [8, 3, 2, 1, 5, 10, -1, -2, 9, 7, 4, -3, 6]
print(quicksort(lista))
