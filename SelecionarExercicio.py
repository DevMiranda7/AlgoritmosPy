import os, random as rd

# 1. Lista todas as pastas dentro do diretório especificado
# Mude conforme o seu caso
pastas = os.listdir("C:/Users/luanm/Documents/LeetCode/Algoritmos")

# 2. Escolhe uma pasta aleatória e lista os arquivos nela
# Mude conforme o seu caso
arquivos = os.listdir("C:/Users/luanm/Documents/LeetCode/Algoritmos/" + rd.choice(pastas))

# 3. Escolhe um arquivo aleatório da pasta e remove a extensão ".py" para exibir só o nome
print(rd.choice(arquivos).replace(".py", " "))

