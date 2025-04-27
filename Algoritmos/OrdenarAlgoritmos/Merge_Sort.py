# Merge Sort

# Função principal que implementa o algoritmo Merge Sort
def merge_sort(lista):
    # Caso base: se a lista tiver 1 ou 0 elementos, já está ordenada
    if len(lista) <= 1:
        return lista
    
    # Encontrar o meio da lista para dividir em duas partes
    mid = len(lista) // 2

    # Recursivamente, aplica merge_sort na metade esquerda
    esquerda = merge_sort(lista[:mid])
    
    # Recursivamente, aplica merge_sort na metade direita
    direita = merge_sort(lista[mid:])

    # Depois de ordenar as duas metades, junta elas
    return merge(esquerda, direita)

# Função auxiliar que une duas listas ordenadas em uma só
def merge(esquerda, direita):
    # i e j são índices para percorrer as listas esquerda e direita
    i = j = 0

    # Lista que irá armazenar os elementos ordenados
    arrayOrdenado = []

    # Enquanto houver elementos em ambas as listas
    while i < len(esquerda) and j < len(direita):
        # Compara os elementos atuais de esquerda e direita
        if esquerda[i] < direita[j]:
            # Se o elemento da esquerda for menor, adiciona ele
            arrayOrdenado.append(esquerda[i])
            i += 1
        else:
            # Se o elemento da direita for menor ou igual, adiciona ele
            arrayOrdenado.append(direita[j])
            j += 1

    # Após terminar uma das listas, adiciona o restante da outra lista
    arrayOrdenado += (esquerda[i:])
    arrayOrdenado += (direita[j:])

    # Retorna a lista mesclada e ordenada
    return arrayOrdenado

# Lista inicial desordenada
lista = [94, 1, 9, 8]

# Chama a função de ordenação e armazena o resultado
resposta = merge_sort(lista)

# Imprime a lista ordenada
print(resposta)
