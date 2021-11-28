
from random import randint


#Criar jogadas do BOT
itens= ['Pedra', 'Papel','Tesoura']


#Criar jogadas do computador

ganhadorJogo = 0 # 0 = Ninguém, 1 = Computador, 2 = Jogador

scoreJogador = 0

scoreComputador = 0


while ganhadorJogo == 0:
    computador = randint(0, 2)
    print('O computador escolheu {}'.format(itens[computador]))

    print('''Opções: [0] PEDRA
         [1] PAPEL
         [2] TESOURA''')
    jogador= int(input('Qual é a sua jogada?'))

    print('Computador: {}'.format(itens[computador]))
    print('Jogador: {}'.format(itens [jogador]))

    if computador == 0:
        if jogador == 0:
            print('Empate')
        elif jogador == 1:
            print('Jogador ganhou')
            scoreJogador = scoreJogador +1
        elif jogador == 2:
            print('Computador ganhou')
            scoreComputador = scoreComputador +1
        else:
            print('JOGADA INVÁLIDA')
    if computador == 1:
        if jogador == 0:
            print('Computador ganhou')
            scoreComputador = scoreComputador +1
        elif jogador == 1:
            print('Empate')
        elif jogador == 2:
            print('Jogador ganhou')
            scoreJogador = scoreJogador +1
        else:
            print('JOGADA INVÁLIDA')
    if computador == 2:
        if jogador == 0:
            print('Computador ganhou')
            scoreComputador = scoreComputador +1
        elif jogador == 1:
            print('Computador ganhou')
            scoreComputador = scoreComputador + 1
        elif jogador == 2:
            print('Empate')
        else:
            print('JOGADA INVÁLIDA')

    if scoreComputador == 3:


        print('Computador venceu')

        ganhadorJogo = 1


    if scoreJogador == 3:

        print('Jogador venceu')

        ganhadorJogo = 2


