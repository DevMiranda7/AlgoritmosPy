# Fibonacci Recursivo

# Função recursiva que calcula o n-ésimo número de Fibonacci
def fibonacci(n):
    # Caso base: se n for 0 ou 1, o número de Fibonacci é igual a n
    if n == 0 or n == 1:
        return n
    # Recursão: soma os dois números anteriores na sequência
    return fibonacci(n-1) + fibonacci(n-2)

# Chama a função fibonacci para calcular o número de Fibonacci na posição 10
resposta = fibonacci(10)

# Imprime o resultado
print(resposta)



# Números de Fibonacci para confirmar o resultado anterior.

# Inicialização dos dois primeiros números da sequência de Fibonacci
numero_atual = 0
numero_proximo = 1
quantidade_de_elementos = 12  # <-- Número de elementos que serão gerados na sequência de Fibonacci, caso o número seja grande, insira um valor maior!

# Laço para gerar os primeiros quantidade_de_elementos números de Fibonacci
for i in range(quantidade_de_elementos):
    print(numero_atual, end=",")  # Imprime o número atual da sequência
    numero_sucessor = numero_atual + numero_proximo  # Calcula o próximo número da sequência
    numero_atual = numero_proximo  # Atualiza o valor do número_atual para o próximo número
    numero_proximo = numero_sucessor  # Atualiza o valor de numero_proximo para o próximo número


