def fatorial(n):
    print(f"Fatorial: {n}")
    if n == 1:
        return n
    return n*fatorial(n-1)

resposta = fatorial(5)
print(resposta)