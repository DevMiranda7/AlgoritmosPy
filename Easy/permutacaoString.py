def permutacao(string,passo):
    if passo == len(string):
        for c in string:
            print(c,end="")
        print()
        return
    
    for i in range(passo,len(string)):

        temporaria = string[passo]
        string[passo] = string[i]
        string[i] = temporaria


        permutacao(string,passo+1)


        temporaria = string[passo]
        string[passo] = string[i]
        string[i] = temporaria




lista=[]
entrada = "abc"

for i in entrada:
    lista.append(i)


permutacao(lista,0)