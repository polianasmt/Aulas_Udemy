nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = int(input("Digite seu peso: "))

imc =  peso / (altura ** 2) 

print("Seu imc é: {:.2f}".format(imc))