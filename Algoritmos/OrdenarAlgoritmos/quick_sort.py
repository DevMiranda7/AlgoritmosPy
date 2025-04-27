# Quick Sort

# Função que implementa o algoritmo QuickSort
def quicksort(arry, inicio, fim):
    # Caso base: se a lista tiver apenas um elemento ou estiver vazia, a recursão termina
    if inicio < fim:
        # Encontra o índice do pivô e divide a lista em duas sublistas
        pivo = particao(arry, inicio, fim)
        
        # Ordena a sublista à esquerda do pivô
        quicksort(arry, inicio, pivo - 1)
        
        # Ordena a sublista à direita do pivô
        quicksort(arry, pivo + 1, fim)

# Função que realiza a partição da lista, escolhendo um pivô e rearranjando os elementos
def particao(arry, inicio, fim):
    # Escolhe o último elemento da lista como pivô
    pivo = arry[fim]
    # Inicializa o índice i antes do primeiro elemento da lista
    i = inicio - 1

    # Percorre a lista, comparando os elementos com o pivô
    for j in range(inicio, fim):
        # Se o elemento atual for menor ou igual ao pivô
        if arry[j] <= pivo:
            i += 1
            # Troca o elemento arry[i] com arry[j]
            arry[i], arry[j] = arry[j], arry[i]
    
    # Coloca o pivô no lugar correto, trocando o arry[i+1] com o arry[fim]
    arry[i+1], arry[fim] = arry[fim], arry[i+1]
    
    # Retorna o índice do pivô
    return i + 1 

# Lista desordenada de letras
lista = ["d", "a", "h", "b", "c"]

# Chama a função quicksort para ordenar a lista
quicksort(lista, 0, len(lista) - 1)

# Imprime a lista ordenada
print(lista)
