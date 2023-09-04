def soma(lista):
    # caso base
    if not lista: 
        return 0

    # caso recursivo
    return lista[0] + soma(lista[1:])

lista = [8, 1, 2]
print(soma(lista))
