def buscaBinaria(lista,alvo):
    inicio = 0
    fim = len(lista)-1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1
lista = [5,13,80,90,91,77,1000]

print(buscaBinaria(lista,1000))