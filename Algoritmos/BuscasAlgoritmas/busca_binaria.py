# Função de busca:

def buscaBinaria(lista,alvo):
    inicio = 0
    fim = len(lista)-1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return f"Encontrado no index: {meio}"
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1
lista = [5,13,80,90,91,77,100,542,563,1232]

print(buscaBinaria(lista,100))