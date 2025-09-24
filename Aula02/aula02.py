from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

continuar = input('Você quer jogar Jokenpô? (S/N) ').strip().upper()

while continuar == 'S':
    print('''Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')

    jogador = int(input('Qual é a sua jogada? '))
    print('-=' * 11)
    print(f'O computador escolheu {itens[computador]}')
    print(f'O jogador escolheu {itens[jogador]}')
    print('-=' * 11)

    if computador == 0:  # computador jogou PEDRA
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('JOGADOR VENCE')
        elif jogador == 2:
            print('COMPUTADOR VENCE')
        else:
            print('JOGADA INVÁLIDA! TENTE NOVAMENTE.')
    elif computador == 1:  # computador jogou PAPEL
        if jogador == 0:
            print('COMPUTADOR VENCE')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('JOGADOR VENCE')
        else:
            print('JOGADA INVÁLIDA! TENTE NOVAMENTE.')
    elif computador == 2:  # computador jogou TESOURA
        if jogador == 0:
            print('JOGADOR VENCE')
        elif jogador == 1:
            print('COMPUTADOR VENCE')
        elif jogador == 2:
            print('EMPATE')
        else:
            print('JOGADA INVÁLIDA! TENTE NOVAMENTE.')
    continuar = input('Você quer jogar novamente? (S/N) ').strip().upper()
print('Jogo encerrado. Até a próxima!')