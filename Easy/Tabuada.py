def tabuada(numero):
    for i in range(10):
        print(f"{numero} x {i+1} = {numero*(i+1)}")
        
tabuada(int(input("Digite qualquer numero para exibir a tabuada correspondente:")))