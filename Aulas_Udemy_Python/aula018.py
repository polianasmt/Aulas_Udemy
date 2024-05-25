"""
Cuidados com dados mutáveis

= - copiando o valor(imutáveis)
= - aponta para o mesmo valor na memória(mutável)

para "copiarmos" os dados de uma lista, utiliza-se copy()
"""

lista_a = ['Poliana', 'Henrique', '']
lista_b = lista_a.copy()

lista_a[2] = 'Amor'

print(lista_a)
print(lista_b)