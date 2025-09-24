import random

# todo (lista de tarefas)
listaTarefas = [

]
for tarefa in range (1, 6): #! Se eu quiser 5 tarefas preciso deixar o range como 1, 6
    novaTarefa = input(f'Digite a tarefa {tarefa}: ')
    listaTarefas.append(novaTarefa)
    for tarefa in listaTarefas:
        print(f'- {tarefa}')


# todo (range de números ímpares)
listaNumeros = [

]
for numero in range (1, 2001):
    if numero % 2 != 0:
        listaNumeros.append(numero)
print(listaNumeros)


# todo (escolha de números aleatórios)
listaAleatorios = [

]
iniciar = input('Você quer gerar uma lista de 10 números aleatórios entre 1 e 100? (S/N) ').strip().upper()
if iniciar == 'S':
    for aleatorio in range (1, 11):
        numeroAleatorio = random.randint(1, 100)
        listaAleatorios.append(numeroAleatorio)
    print(listaAleatorios)
else:
    print('Programa encerrado. Até a próxima!')


# todo (mini lista de compras)
listaCompras = []

for i in range(1, 11):
    novoitem = input(f'Digite o item {i} da sua lista de compras: ')
    if novoitem in listaCompras:
        adicionarNovamente = input(f'O item "{novoitem}" já está na sua lista de compras, deseja adicionar novamente? (S/N) ').strip().upper()
        if adicionarNovamente == 'S':
            listaCompras.append(novoitem)
            print(f'O item "{novoitem}" foi adicionado {listaCompras.count(novoitem)} vezes na sua lista de compras.')
    else:
        listaCompras.append(novoitem)

print('Sua lista de compras:')
for item in listaCompras:
        print(f' - {item}')




