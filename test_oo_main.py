from .test_oo import JogodaVelha

humano_escolha, bot_escolha, dificuldade = '','','',

jogo = JogodaVelha(humano_escolha, bot_escolha, dificuldade)

while humano_escolha != 'O' and humano_escolha != 'X':
    try:
        print('')
        print('Bem vindo ao jogo da velha, professor Allan!')
        humano_escolha = input('Escolha X or O: ').upper()
    except (EOFError, KeytabuleiroInterrupt):
        print('Byeeeee')
        exit()
    except (KeyError, ValueError):
        print('Tente novamente!')

if humano_escolha == 'X':
    bot_escolha = 'O'
else:
    bot_escolha = 'X'

while dificuldade != '1' and dificuldade != '2' and dificuldade != '3':
    try:
        dificuldade = input('Escolha sua dificuldade: \nFácil[1]\nMédio[2]\nDifícil[3]\n').upper()
    except (EOFError, KeytabuleiroInterrupt):
        print('Byeeeee')
        exit()
    except (KeyError, ValueError):
        print('Tente novamente!')

primeiro_movimento = 'H'
while len(celulas_vazias(tabuleiro)) > 0 and not game_over(tabuleiro):
    if primeiro_movimento:
        vez_bot(bot_escolha, humano_escolha, dificuldade)
        primeiro_movimento = ''

    vez_humano(bot_escolha, humano_escolha)
    vez_bot(bot_escolha, humano_escolha, dificuldade)

if wins(tabuleiro, jogo.HUMANO):

    print(f'Sua vez[{humano_escolha}]')
    mostra_tabuleiro(tabuleiro, bot_escolha, humano_escolha)
    print('Você ganhou, aff...')
elif wins(tabuleiro, BOT):

    print(f'Minha vez! Deixe eu pensar... [{bot_escolha}]')
    mostra_tabuleiro(tabuleiro, bot_escolha, humano_escolha)
    print('Perdeste! Hahah')
else:

    mostra_tabuleiro(tabuleiro, bot_escolha, humano_escolha)
    print('Ih, deu velha...')

exit()
