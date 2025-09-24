
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


