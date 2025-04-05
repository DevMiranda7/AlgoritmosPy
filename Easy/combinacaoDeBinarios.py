def gerar_binarios(n, atual=""):
    if len(atual) == n:
        print(atual)
        return

    gerar_binarios(n, atual + "0")
    gerar_binarios(n, atual + "1")

# Teste
gerar_binarios(3)