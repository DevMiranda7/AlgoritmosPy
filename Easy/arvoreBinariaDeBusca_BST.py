class No:
    def __init__(self,valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def inserir(raiz,valor):
    if raiz is None:
        return No(valor)
    if valor < raiz.valor:
        raiz.esquerda = inserir(raiz.esquerda,valor)
    else:
        raiz.direita = inserir(raiz.direita,valor)
    return raiz


def busca(raiz,valor):
    if raiz is None:
        return False
    if raiz.valor == valor:
        return True
    elif valor < raiz.valor:
        return busca(raiz.esquerda,valor)
    else:
        return busca(raiz.direita,valor)

valores = [1,2,3,4,5,6,7,8,9,10]
raiz = None
for valor in valores:
    raiz = inserir(raiz,valor)

print(busca(raiz,10))
print(busca(8,2))