def encontrar_numeros_repetidos(a, b):
    numeros_repetidos = []
    
    for numero in a:
        if numero in b and numero not in numeros_repetidos:
            numeros_repetidos.append(numero)
    
    return numeros_repetidos

# Vetores de entrada
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
b = [4, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]

# Chamar a função para encontrar os números repetidos
numeros_repetidos = encontrar_numeros_repetidos(a, b)

# Exibir os valores do terceiro vetor
print(numeros_repetidos)
