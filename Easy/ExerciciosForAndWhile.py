# #Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.

inicio = int(input("Digite o número inicial:"))
final = int(input("Digite o número final:"))
print(" ")
print(f"Números entre {inicio} e {final}")
for numeros in range(inicio+1,final):
    
    print(numeros)





#3) Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas são válidas. 
# Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido.
#  Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.


dados = 15
avaliacoes = 0
contador = 0
while contador < dados:
    notas = int(input("Digite a sua avaliação sobre o serviço prestado: "))
    if notas >= 0 and notas <=5:
        avaliacoes += notas
        contador+=1    
    else:
        print("Nota inválida, tente novamente.")
        contador-1

print(f"Média da empresa: {avaliacoes/dados}")
