#operadores logicos: and, or e not

login = input("[E]ntrar     [S]air: ")
senha = input("Senha: ")

senha_permitida = '12345'

if (login == "E" or login == "e") and senha == senha_permitida:
    print("Login sucedido")

else: 
    print("Senha incorreta")