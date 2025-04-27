# Função que faz a contagem regressiva a partir de um número
def contagem(start):
    print("Contagem regressiva")  # Exibe a mensagem inicial
    # Laço de repetição que vai de 'start' até 0, decrementando 1 a cada iteração
    for i in range(start, -1, -1):
        print(f"Tempo: {i}")  # Imprime o valor atual da contagem

# Solicita o valor do usuário e chama a função de contagem
contagem(int(input("Valor: ")))  # Converte a entrada do usuário para inteiro e passa para a função
