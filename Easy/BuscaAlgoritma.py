lista = [1,5,2,2,200,54,99,77,9,41,52,38,74,540]
def buscarAlgoritmo(list,valor):
    for i in range(len(list)):
        if list[i] == valor:
            print(f"Número encontrado: {list[i]}")  
            return i
    return -1   
        


valor = 74
resposta = buscarAlgoritmo(lista,valor)

print(resposta)