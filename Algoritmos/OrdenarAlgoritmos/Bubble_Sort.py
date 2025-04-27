#Bubble Sort

# Lista de letras desordenadas
letras = ["D", "C", "F", "G", "H", "E", "A", "B"]

# Armazena o tamanho da lista
tamanho = len(letras)

# Laço externo: controla o número de passagens pela lista
for i in range(tamanho - 1):
    # Laço interno: percorre a lista até o penúltimo elemento não ordenado
    for j in range(tamanho - 1 - i):
        # Compara dois elementos adjacentes
        if letras[j] > letras[j + 1]:
            # Se estiverem fora de ordem, troca eles de lugar
            temporaria = letras[j]
            letras[j] = letras[j + 1]
            letras[j + 1] = temporaria

# Após a ordenação, imprime cada letra na ordem correta
for i in range(tamanho):
    print(letras[i])
