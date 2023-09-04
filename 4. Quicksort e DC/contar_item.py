def contar(lista):
    # caso base
    if not lista:
        return 0
    
    # caso recursivo
    return 1 + contar(lista[1:])

lista = [1, 3, 5, 7, 9, 4]

print(contar(lista))