"""
Listas em python
tipo list - mutável
suporta vários valores de qualquer tipo
conhecimentos reutilizaveis - indices de fatiamento
métodos uteis: append, insert, pop, del, clear, extend +
create, read, update, delete (CRUD)

append - adiciona um item ao final
insert - adiciona um item no indice escolhido
pop - remove do final ou do indice escolhido
del - apaga um indice
clear - limpa a lista
extend - estende a lista

+ - concatena listas
"""

lista= [123, True, 'Olá', 1.02, []]

del lista[1]

lista.append(50)
lista.pop()
lista.append('Poliana')
lista.append(56)

ultimo_valor = lista.pop(2)
print(lista, 'removido', ultimo_valor)

