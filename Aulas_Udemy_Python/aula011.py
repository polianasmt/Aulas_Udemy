#mostre qual letra apareceu mais na string 

frase = input("Escreva uma frase: ")

i = 0
mais_vezes = 0
letra_mais_vezes = ''

while i < len(frase):
    letra = frase[i]
    qnts_letras = frase.count(letra)

    if letra_mais_vezes == ' ':
        i += 1
        continue

    if mais_vezes < qnts_letras:
        mais_vezes = qnts_letras
        letra_mais_vezes = letra

    i += 1

print("A letra que mais apareceu foi '{}' e apareceu {}x".format(letra_mais_vezes, mais_vezes))

print("A letra que apareceu mais vezes foi", letra_mais_vezes, "e apareceu", mais_vezes)