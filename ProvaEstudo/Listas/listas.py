lista = [  # ! lista de strings básicas
    "banana", "maçã", "laranja", "uva", "pera"
]
print(lista)
print(type(lista)) 

# todo (listas podem ter tipos variados)
lista2 = [
    "banana", 3.5, True, 10, [1, 2, 3]  # ! lista com tipos variados
]
print(lista2)
print(type(lista2))

# todo (.extend)
lista2.extend([4, 5, 6])  # ! adiciona elementos ao final da lista
print(lista2)

lista += [7, 8, 9]  # ! outra forma de adicionar elementos
print(lista2)

# todo (.insert)
lista3 = [
    "banana", "maçã", "laranja", "uva", "pera"
]
lista3.insert(1, "abacaxi")  # ! insere elemento na posição desejada
print(lista3)

# todo (.remove)
lista4 = [
    1 , 2, 3, 4, 5
]
lista4.remove(3)  # ! remove o elemento pelo valor
print(lista4)

# todo (.pop)
lista5 = [
    20, 30, 40, 50, 60
]
lista5.pop()  # ! remove o último elemento
print(lista5)

# todo (verificar se o elemento está ou não na lista)
lista6 = [
    "banana", "maçã", "laranja", "uva", "pera"
]
print("maçã" in lista6)  # ! verifica se o elemento está na lista 
print("abacaxi" not in lista6) # ! verifica se o elemento não está na lista

# todo (len)
lista7 = [
    "banana", "maçã", "laranja", "uva", "pera"
]
print(len(lista7))  # ! retorna o tamanho da lista

# todo (count)
lista8 = [
    1, 2, 3, 4, 5, 1, 2, 1
]
print(lista8.count(1))  # ! conta quantas vezes o elemento aparece na lista

# todo (append)
listaappend = [
    "banana", "maçã", "laranja"
]
listaappend.append("uva")  # ! adiciona elemento ao final da lista
print(listaappend)

# todo (index)
lista9 = [
    "banana", "maçã", "laranja", "uva", "pera"
]
print(lista9.index("laranja"))  # ! retorna o índice do elemento

# todo (sort)
lista10 = [
    5, 3, 1, 4, 2
]
lista10.sort()  # ! ordena a lista em ordem crescente
print(lista10)

# todo (reverse)
lista11 = [
    1, 2, 3, 4, 5
]
lista11.reverse()  # ! inverte a ordem da lista
print(lista11)

# todo (for com lista)
lista12 = [
    "banana", "maçã", "laranja", "uva", "pera"
]
for fruta in lista12:
    print(fruta)  # ! itera sobre os elementos da lista