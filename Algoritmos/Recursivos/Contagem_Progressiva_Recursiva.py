# Função recursiva que realiza uma contagem progressiva até 10
def contagemProgressiva(n):
    # Caso base: se n for igual a 10, a contagem para
    if n == 10:
        return n
    print(n,end=" ")  # Imprime o valor atual
    # Chama recursivamente a função, incrementando n
    return contagemProgressiva(n + 1)

# Chama a função de contagem progressiva começando de 0
resposta = contagemProgressiva(0)

# Imprime o valor retornado pela função (será 10, pois esse é o valor retornado no caso base)
print(resposta)
