def converter_nota_romana(nota):
    notas = {
        "Dó": "I",
        "Ré": "II",
        "Mi": "III",
        "Fá": "IV",
        "Sol": "V",
        "Lá": "VI",
        "Si": "VII"
    }
    return notas.get(nota, "Nota(s) inválida(s)")

# Exemplo de uso
entrada = input("Digite as notas musicais separadas por virgula: ")
notas_musicais = entrada.split(',')

saida = list(map(converter_nota_romana, notas_musicais))
print("Saída:", " ".join(saida))