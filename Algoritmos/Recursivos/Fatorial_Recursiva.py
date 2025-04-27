# Função recursiva para calcular o fatorial de um número
def fatorial(n):
    print(f"Fatorial: {n}")  # Exibe o valor de n a cada chamada recursiva
    # Caso base: se n for igual a 1 ou 0, o fatorial é 1
    if n == 0 or n == 1:
        return 1
    # Recursão: multiplica n pelo fatorial do número anterior
    return n * fatorial(n - 1)

# Chama a função para calcular o fatorial de 5
resposta = fatorial(5)

# Imprime o resultado
print(f"Resutlado: {resposta}")
