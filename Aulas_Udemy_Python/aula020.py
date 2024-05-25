#Enumerate - enumera iteraveis(indices)

lista = ['A', 'B', 'C']

for item in enumerate(lista):
    print(item)

for indice, nome in enumerate(lista):
    print(indice, nome)

for item in enumerate(lista):
    indice, nome = item
    print(item)

#\t da tab