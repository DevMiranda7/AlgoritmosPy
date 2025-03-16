def contagemRegressiva(n):
    
    if n == 0:
        return n
    print(n)
    return contagemRegressiva(n-1)

resposta = contagemRegressiva(10)
print(resposta)