contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print("Não vou mostrar o 6")
        continue #continue é utilizado para pular um trecho do código, como por exemplo, aqui ele vai pular o número 6

    print(contador)

    if contador == 40:
        break #break é utilizado para quebrar o loop