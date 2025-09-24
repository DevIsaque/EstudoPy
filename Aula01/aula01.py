def processo_financiamento():
    dinheiro = int(input("Qual é o seu salário mensal? R$ "))
    ano = int(input("Quantos anos você pretende financiar? "))
    parcela = int(input("Qual o valor da parcela que você pode pagar mensalmente? R$ "))
    trinta_porcento = dinheiro * 0.30

    if parcela > trinta_porcento:
        print(f"Seu financiamento não foi aprovado, {nome}. A parcela de R$ {parcela:.2f} excede 30% do seu salário.")
        return

    mensalidades = ano * 12 
    valor_casa = parcela * mensalidades

    if escolha == '1':
        if valor_casa >= 1000000:
            print("Parabéns, você financiou a Casa Grande!")
        else:
            print("Desculpe, o valor da parcela não é suficiente para financiar a Casa Grande.")
    elif escolha == '2':
        if valor_casa >= 500000:
            print("Parabéns, você financiou a Casa Média!")
        else:
            print("Desculpe, o valor da parcela não é suficiente para financiar a Casa Média.")
    elif escolha == '3':
        if valor_casa >= 250000:
            print("Parabéns, você financiou a Casa Pequena!")
        else:
            print("Desculpe, o valor da parcela não é suficiente para financiar a Casa Pequena.")
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
        return


# Programa principal
nome = str(input('Qual é o seu nome? '))

lista_casas = {
    'casa1': ' 1 Casa Grande (R$ 1.000.000,00)',
    'casa2': ' 2 Casa Média (R$ 500.000,00)',
    'casa3': ' 3 Casa Pequena (R$ 250.000,00)'
}

print(f'\nOlá, {nome}! Seja bem-vindo(a) ao nosso sistema de venda de casas.')
print('Aqui estão as opções de casas disponíveis para você:')
for casa, descricao in lista_casas.items():
    print(f'- {descricao}')

escolha = input('\nDigite o número da casa que você deseja comprar (1, 2 ou 3): ')

continuar = input('\nDeseja continuar? (S/N) ').strip().upper()
if continuar == 'S':
    processo_financiamento()
else:
    print("Programa encerrado. Até logo!")








    


