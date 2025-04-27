# Permutação de Strings

# Função que gera todas as permutações de uma string
def permutacao(string, passo):
    # Caso base: quando o índice 'passo' for igual ao tamanho da string,
    # todas as posições foram permutadas, então imprime a string
    if passo == len(string):
        for c in string:
            print(c, end="")  # Imprime a string permutada
        print()  # Imprime uma nova linha após a permutação
        return
    
    # Laço para gerar todas as permutações
    for i in range(passo, len(string)):
        # Troca o elemento na posição 'passo' com o elemento na posição 'i'
        temporaria = string[passo]
        string[passo] = string[i]
        string[i] = temporaria

        # Chama recursivamente a função para permutar os próximos elementos
        permutacao(string, passo + 1)

        # Desfaz a troca (backtracking), revertendo a string para a forma original
        temporaria = string[passo]
        string[passo] = string[i]
        string[i] = temporaria

# Lista que armazenará os caracteres da string de entrada
lista = []

# Entrada: string a ser permutada
entrada = "ABC"

# Converte a string de entrada em uma lista de caracteres
for i in entrada:
    lista.append(i)

# Chama a função de permutação para gerar todas as permutações
permutacao(lista, 0)
