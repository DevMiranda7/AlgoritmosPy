#Fibonacci
anterior = 0
proximo = 1
quantidadeDeNumeros = 15
for i in range(quantidadeDeNumeros):
    print(anterior)

    soma = anterior + proximo
    anterior = proximo
    proximo = soma

# contagem Progressiva
def contagemProgressiva(numero_inicial,numero_final):
    if numero_inicial == numero_final:
        return numero_inicial
    print(numero_inicial)
    return contagemProgressiva(numero_inicial+1,numero_final)

resposta = contagemProgressiva(0,20)
print(resposta)

# busca Algoritma Enumerate
listaIndexs=[]
def buscaAlgoritmaEnumerate(lista,valor):
    
    for i, elemento, in enumerate(lista):
        if elemento == valor:
            print(f"Elemento encontrado: {elemento} no index: {i}")
            listaIndexs.append(i)
    print(f"Indexs: {listaIndexs}")
    return valor
            
            
        

listaa=[0,1,5,2,3,2,10,22,33,44,11,44,77,2,90]
chave = 2

resposta = buscaAlgoritmaEnumerate(listaa,chave)
print(resposta)

# BubbleSort
string = ["B","A","C"]
tamanho = len(string)

for i in range(tamanho-1):
    for j in range(tamanho - 1 - i):
        if string[j] > string [j+1]:
            temp = string[j]
            string[j] = string[j+1]
            string[j+1] = temp


for i in string:
    print(i)

