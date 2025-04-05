def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    mid = len(lista) // 2

    esquerda = merge_sort(lista[:mid])
    direita = merge_sort(lista[mid:])

    return merge(esquerda,direita)


def merge(esquerda, direita):

    i = j = 0

    arrayOrdenado = []

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            arrayOrdenado.append(esquerda[i])
            i += 1
        else:
            arrayOrdenado.append(direita[j])
            j += 1

    

    arrayOrdenado += (esquerda[i:])
    arrayOrdenado += (direita[j:]) 

    return arrayOrdenado

lista = [94,1,9,8]
resposta= merge_sort(lista)
print(resposta)