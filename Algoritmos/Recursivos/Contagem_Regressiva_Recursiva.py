# Função recursiva que realiza uma contagem regressiva até 0
def contagemRegressiva(n):
    # Caso base: se n for igual a 0, a contagem para
    if n == 0:
        return n  # Retorna 0, que é o caso base
    print(n,end=" ")  # Imprime o valor atual
    # Chama recursivamente a função, decrementando n
    return contagemRegressiva(n - 1)

# Chama a função de contagem regressiva começando de 10
resposta = contagemRegressiva(10)

# Imprime o valor retornado pela função (será 0, pois esse é o valor retornado no caso base)
print(resposta)
