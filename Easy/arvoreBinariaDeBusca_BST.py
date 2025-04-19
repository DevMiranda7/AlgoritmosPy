#APRENDENDO


# class No:
#     def __init__(self, valor):
#         self.valor = valor      # O valor armazenado no nó
#         self.esq = None         # Ponteiro para o nó da esquerda
#         self.dir = None         # Ponteiro para o nó da direita

# def inserir(raiz, valor):
#     if raiz is None:
#         return No(valor)
#     if valor < raiz.valor:
#         raiz.esq = inserir(raiz.esq, valor)
#     else:
#         raiz.dir = inserir(raiz.dir, valor)
#     return raiz


# def buscar(raiz, alvo):
#     if raiz is None:
#         return False
#     if raiz.valor == alvo:
#         return True
#     elif alvo < raiz.valor:
#         return buscar(raiz.esq, alvo)
#     else:
#         return buscar(raiz.dir, alvo)

# raiz = None
# valores = [8, 3, 10, 1, 6, 14]
# for v in valores:
#     raiz = inserir(raiz, v)

# print(buscar(raiz, 6))   # True
# print(buscar(raiz, 7))   # False
