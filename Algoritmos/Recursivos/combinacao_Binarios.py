#Combinação de binários

# Função que gera todos os números binários de n bits
def gerar_binarios(n, atual=""):
    # Caso base: quando a string 'atual' tiver o tamanho n, imprime o número binário
    if len(atual) == n:
        print(atual)
        return

    # Chama a função recursivamente, adicionando '0' à string atual
    gerar_binarios(n, atual + "0")
    
    # Chama a função recursivamente, adicionando '1' à string atual
    gerar_binarios(n, atual + "1")

# Teste: gera todos os números binários de 3 bits
gerar_binarios(3)
