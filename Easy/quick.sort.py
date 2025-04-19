def quicksort(arry,inicio,fim):
    if inicio < fim:
        pivo = particao(arry,inicio,fim)
        quicksort(arry,inicio,pivo-1)
        quicksort(arry,pivo + 1, fim)

def particao(arry,inicio,fim):
    pivo = arry[fim]
    i = inicio - 1

    for j in range(inicio,fim):
        if arry[j] <= pivo:
            i+=1
            arry[i],arry[j] = arry[j],arry[i]
    
    arry[i+1],arry[fim] = arry[fim], arry[i+1]
    return i + 1 



lista = ["d","a","h","b","c"]
quicksort(lista,0,len(lista)-1)

print(lista)