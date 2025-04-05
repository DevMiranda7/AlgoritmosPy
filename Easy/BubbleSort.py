string = [1,0,3,2,9,22,12,33]
tamanho = len(string)

for i in range(tamanho - 1):
    for j in range(tamanho - 1 - i):
        if string[j] > string [j  + 1]:
            temporaria = string[j]
            string[j] = string[j + 1]
            string[j + 1] = temporaria


for i in range(tamanho):
    print(string[i])