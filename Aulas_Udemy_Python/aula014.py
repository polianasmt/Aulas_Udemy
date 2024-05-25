"""
iterável = str, range, etc (___iter___)
iterador = quem sabe entregar um valor por vez
next = me entregue o próximo valor
iter = me entregue seu iterador

"""

# texto = iter("Poliana")

# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))


texto = 'Poliana'
# iterador = iter(texto)

# while True:
#     try: 
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)