import os, random as rd


arquivos = os.listdir("C:/Users/luanm/Documents/LeetCode/Easy")

print(rd.choice(arquivos).replace(".py", " "))