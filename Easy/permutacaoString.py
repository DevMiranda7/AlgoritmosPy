#Permutações de uma String Descrição: Desenvolver um algoritmo recursivo para gerar todas as permutações de uma string dada 
#   (ex: ABC → ABC, ACB, BAC, BCA, CAB, CBA).
#    Objetivo: Aplicar recursividade para explorar as diferentes combinações possíveis de letras.
#    Desafio extra: Trabalhar com strings grandes e contar quantas permutações são possíveis. (0,5 ponto)




def permutacao(prefixo, restante, resultado):
    if not restante:
        resultado.append(prefixo)
        print(restante)
        print(resultado)
        print(prefixo)
    else:
        for i in range(len(restante)):
            print(restante)
            novo_prefixo = prefixo + restante[i]
            print(novo_prefixo)
            novo_restante = restante[:i] + restante[i+1:]
            print(novo_restante)
            permutacao(novo_prefixo,novo_restante,resultado)
            
letras = "abc"
result = []


resposta = permutacao("",letras,result)


print(result)