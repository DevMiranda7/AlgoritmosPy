letras = ["D","C","F","G","H","E","A","B"]
tamanho = len(letras)

for i in range(tamanho - 1):
  for j in range(tamanho - 1 - i):
    if letras[j] > letras[j + 1]:
      temporaria = letras[j]
      letras[j] = letras[j + 1]
      letras[j + 1] = temporaria


for i in range(tamanho):
  print(letras[i])
