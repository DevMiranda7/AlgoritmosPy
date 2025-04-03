#Permutações de uma String Descrição: Desenvolver um algoritmo recursivo para gerar todas as permutações de uma string dada 
#   (ex: ABC → ABC, ACB, BAC, BCA, CAB, CBA).
#    Objetivo: Aplicar recursividade para explorar as diferentes combinações possíveis de letras.
#    Desafio extra: Trabalhar com strings grandes e contar quantas permutações são possíveis. (0,5 ponto)




def permutacoes(string, passo):
    # Se chegou ao final, imprime a permutação
    if passo == len(string):
        for c in string:
            print(c, end="")  # Imprime sem join
        print()  # Pula para a próxima linha
        return

    # Percorre cada posição possível para troca
    for i in range(passo, len(string)):
        # Troca os caracteres manualmente
        temp = string[passo]
        string[passo] = string[i]
        string[i] = temp

        # Chama a função recursivamente para o próximo passo
        permutacoes(string, passo + 1)

        # Reverte a troca para restaurar o estado original
        temp = string[passo]
        string[passo] = string[i]
        string[i] = temp

# Conversão manual da string para lista
s = []
entrada = "ABC"
for c in entrada:
    s.append(c)

# Chamando a função de permutação
permutacoes(s, 0)
