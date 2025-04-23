# # fatorial
# a = 0 
# b = 1
# numerosAParecer = 12

# for i in range(numerosAParecer):
#     print(a)

#     soma = a + b
#     a = b
#     b = soma


# fatorial recursiva

# def fatorialRecursiva(n):
#     if n == 1 or n == 0:
#         return n
#     return fatorialRecursiva(n-1) + fatorialRecursiva(n-2)



# print(fatorialRecursiva(10-1))


# ordenacao


# BUBBLE SORT


# def bubblesort(string):
#     tamanho = len(string)

#     for i in range(tamanho -1):
#         for j in range(tamanho - 1 - i):
#             if string[j] > string[j+1]:
#                 string[j],string[j+1] = string[j+1],string[j]
                
#     for i in range(tamanho):
#         print(string[i])



# lista=["C","B","A"]
# bubblesort(lista)



# def merge_sort(lista):
#     if len(lista) <= 1:
#         return lista
    
#     mid = len(lista) // 2
#     esquerda = merge_sort(lista[:mid])
#     direita = merge_sort(lista[mid:])

#     return merge(esquerda,direita)


# def merge(esquerda,direita):

#     i, j = 0 
#     arrayOrdenado = []

#     while i < len(esquerda) and j < len(direita):
#         if esquerda[i] < direita[j]:
#             arrayOrdenado.append(esquerda[i])
#             i+=1
#         else:
#             arrayOrdenado.append(direita[j])
#             j+=1
        

#     arrayOrdenado.extend(esquerda[i:])
#     arrayOrdenado.extend(direita[j:])

#     return arrayOrdenado

# lista = [9,11,235,4,2,1,0,7,2]
# print(merge_sort(lista))




#permutacao
# def permutacao(string, passo):
#     if passo == len(string):
#         for c in string:
#             print(c,end="")
#         print()
#         return
        
    
#     for i in range(passo,len(string)):
#         string[passo], string[i] = string[i], string[passo]

#         permutacao(string, passo + 1)
    
#         string[passo], string[i] = string[i], string[passo]



# entrada = "ABC"
# string = []
# for i in entrada:
#     string.append(i)

# permutacao(string,0)


# QuickSort

# def quicksort(arry,inicio,fim):
#     if inicio < fim:
#         pivo = permutacao(arry,inicio,fim)
#         quicksort(arry,inicio,pivo - 1)
#         quicksort(arry,pivo+1,fim)


# def permutacao(arry,inicio,fim):
#     pivo = arry[fim]

#     i = inicio - 1

#     for j in range(inicio,fim):
#         if arry[j]<= pivo:
#             i+=1
#             arry[i], arry[j] = arry[j],arry[i]
#     arry[i + 1], arry[fim] = arry[fim],arry[i + 1]

#     return i + 1


# lista = [2,1,23,44,1,2,3,52,32,10,9]

# quicksort(lista,0,len(lista)-1)
# print(lista)

# buscas

#busca linear
# def buscaLinear(lista,valor):
#     for i in range(len(lista)):
#         if lista[i] == valor:
#             return i
#     return -1



# lista = [10,2,4,1,2,95,22,41,0]
# print(buscaLinear(lista,95))


# busca binaria


# def buscaBinaria(lista,valor):
#     inicio = 0 
#     fim = len(lista)-1

#     while inicio <= fim:
#         meio = (inicio + fim) // 2
#         if lista[meio] == valor:
#             return meio
#         elif lista[meio] > valor:
#             inicio = meio + 1
#         else:
#             fim = meio - 1
#     return -1

# lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# print(buscaBinaria(lista,11))



# def binariosCombination(n,atual=""):
#     if len(atual) == n:
#         print(atual,end="")
#         print()
#         return
#     binariosCombination(n,atual + "0")
#     binariosCombination(n,atual + "1")


# binariosCombination(3,atual="")




# arvore binaria - fácil:


