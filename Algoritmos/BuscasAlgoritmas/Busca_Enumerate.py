def ordenacaoEnumerate(lista, chave):
    for index, elementos in enumerate(lista):
        if elementos == chave:
            return f"Encontrado no index: {index}"
    return -1

lista = [1,5,2,2,200,54,99]


print(ordenacaoEnumerate(lista,5))