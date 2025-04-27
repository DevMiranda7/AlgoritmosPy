# Classe que representa um nó da árvore binária
class No:
    def __init__(self, valor):
        self.valor = valor  # O valor armazenado no nó
        self.esquerda = None  # Ponteiro para o filho à esquerda
        self.direita = None  # Ponteiro para o filho à direita

# Função para inserir um valor na árvore binária
def inserir(raiz, valor):
    # Se a árvore estiver vazia, cria um novo nó
    if raiz is None:
        return No(valor)
    
    # Se o valor for menor que o valor da raiz, insere à esquerda
    if valor < raiz.valor:
        raiz.esquerda = inserir(raiz.esquerda, valor)
    # Se o valor for maior ou igual, insere à direita
    else:
        raiz.direita = inserir(raiz.direita, valor)
    
    # Retorna a raiz da árvore (ou subárvore) atualizada
    return raiz

# Função para buscar um valor na árvore binária
def busca(raiz, valor):
    # Se a raiz for None, significa que a árvore (ou subárvore) está vazia
    if raiz is None:
        return False
    
    # Se o valor for igual ao valor do nó atual, encontramos o valor
    if raiz.valor == valor:
        return True
    
    # Se o valor for menor, a busca continua à esquerda
    elif valor < raiz.valor:
        return busca(raiz.esquerda, valor)
    
    # Se o valor for maior, a busca continua à direita
    else:
        return busca(raiz.direita, valor)

# Lista de valores para inserir na árvore
valores = [5, 4, 3, 2, 1]
raiz = None

# Insere os valores na árvore binária
for valor in valores:
    raiz = inserir(raiz, valor)

# Testa a busca na árvore
print(busca(raiz, 3))  # Deve retornar True, pois 3 está na árvore
print(busca(raiz, 4))  # Deve retornar True, pois 4 está na árvore
