# Função que calcula o fatorial de um número de forma iterativa
def fatorial(n):
    fatorialR = 1  # Inicializa o valor do fatorial como 1
    # Laço de repetição que vai de n até 2, multiplicando os valores
    for i in range(n, 1, -1):
        fatorialR *= i  # Multiplica o fatorial pelo valor atual de i
    print(fatorialR)  # Imprime o valor final do fatorial

# Solicita o valor do usuário e chama a função de cálculo do fatorial
fatorial(int(input("Digite qualquer valor: ")))
