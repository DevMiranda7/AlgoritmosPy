# num1 = int(input("Digite um valor: "))
# num2 = int(input("Digite outro valor: "))
# operacao = input("Digite uma operação matemática: \'*\' \'/\' \'+\' \'-\' \n")
# resultado = 0
# if operacao == "*":
#     resultado = num1*num2
#     print(f"{num1}x{num2} = {resultado}")
# elif operacao == "+":
#     resultado = num1+num2
#     print(f"{num1}+{num2} = {resultado}")
# elif operacao == "-":
#     resultado = num1-num2
#     print(f"{num1}-{num2} = {resultado}")
# elif operacao == "/":
#     resultado = num1/num2
#     print(f"{num1}÷{num2} = {resultado}")
# else:
#     print("Operação desconhecida!")

# if resultado < 0:
#     print("Valor negativo")
# else:
#     print("Valor positivo")

# if "." in str(resultado):
#     print("Resultado é decimal")
# else:
#     print("Resultado inteiro")
#     if resultado % 2 == 0:
#         print("Resultado é Par")
#     else:
#         print("Resultado Impar")



#11) Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo.
#O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno.
#Tenha em mente algumas dicas:

#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes.

# a = int(input("Digite o valor do lado A"))
# b = int(input("Digite o valor do lado B"))
# c = int(input("Digite o valor do lado C"))
# if a > 0 and b > 0 and c > 0:
#     if a == b == c:
#         print("Triângulo Equilátero")
#     elif a == b or a == c or b == a or b == c or c == a or c == b:
#         print("Triângulo Isósceles")
#     elif a != b or a != c or b != c or b != a or c != a or c != b:
#         print("Triângulo Escaleno")
# else:
#     print("Valores inválidos para formar um triângulo")

#12) Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, 
# o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel,
#  se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro.
#  O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70.
#  Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel)
#  e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:

#O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
#O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.