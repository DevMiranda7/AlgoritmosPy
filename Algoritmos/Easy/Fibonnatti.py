# Inicialização dos dois primeiros números da sequência de Fibonacci
numero_atual = 0
numero_proximo = 1
quantidade_de_elementos = 12  # Número de elementos que serão gerados na sequência de Fibonacci

# Laço para gerar os primeiros quantidade_de_elementos números de Fibonacci
for i in range(quantidade_de_elementos):
    print(numero_atual,end=",")  # Imprime o número atual da sequência
    numero_sucessor = numero_atual + numero_proximo  # Calcula o próximo número da sequência
    numero_atual = numero_proximo  # Atualiza o valor do número_atual para o próximo número
    numero_proximo = numero_sucessor  # Atualiza o valor de numero_proximo para o próximo número
