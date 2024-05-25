import os
import random

palavra_secreta = ['python', 'programacao', 'ciencia', 'jogos', 'faculdade', 'estudos']
palavra_aleatoria = random.choice(palavra_secreta)

tamanho_palavra = len(palavra_aleatoria)

palavra_corrente = ['*'] * tamanho_palavra
num_tentativas = 0

print("O tamanho da palavra é {}".format(tamanho_palavra))
print("\n")

acertos = 0;

while(True):
    letra = input("Digite uma letra: ").lower()
    num_tentativas += 1

    try: 
        if len(letra) > 1:
            print("Digite apenas uma letra!")
            continue  

        for i in range(tamanho_palavra): 
            if palavra_aleatoria[i] == letra:
                palavra_corrente[i] = letra
                acertos += 1
        print(palavra_corrente)

        if acertos == len(palavra_aleatoria):
            #os.system('cls')
            print("\n")
            print("Parabéns! Você acertou, a palavra secreta era '{}'".format(palavra_aleatoria))
            print("Número de tentativas: {}".format(num_tentativas))
            print("\n")
            num_tentativas = 0

    except:
        print("erro")

    
        
