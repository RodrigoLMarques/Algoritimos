# Minha solução prévia
def mymaximo(lista):
    # caso base
    if len(lista) == 1:
        return lista[0]
    
    # caso recursivo
    if lista[0] > lista[1]:
        lista[1] = lista[0]
        return maximo(lista[1:])
    
    return maximo(lista[1:])


def maximo(lista):
    # caso base
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    
    # caso recursivo
    sub_max = maximo(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max

lista = [1, 3, 2, 4, 5, 8, 4]

print(maximo(lista))