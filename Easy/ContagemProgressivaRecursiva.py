def contagemProgressiva(n):
    if n == 10:
        return n
    print(n)
    return contagemProgressiva(n+1)
    
resposta = contagemProgressiva(0)

print(resposta)