from jogo_da_velha import JogodaVelha

humano_escolha, bot_escolha, dificuldade = '','','',

while humano_escolha != 'O' and humano_escolha != 'X': # escolha do x ou o e dificuldade
    try:
        print('')
        print('Bem vindo ao jogo da velha, professor Allan!')
        humano_escolha = input('Escolha X or O: ').upper()
    except (KeyError, ValueError):
        print('Tente novamente!')

if humano_escolha == 'X':
    bot_escolha = 'O'
else:
    bot_escolha = 'X'

while dificuldade != '1' and dificuldade != '2' and dificuldade != '3':
    try:
        dificuldade = input('Escolha sua dificuldade: \nFácil[1]\nMédio[2]\nDifícil[3]\n').upper()
    except (KeyError, ValueError):
        print('Tente novamente!')

jogo = JogodaVelha(humano_escolha, bot_escolha, dificuldade) #inicio das jogadas

primeiro_movimento = 'H'
while len(jogo.celulas_vazias(jogo.tabuleiro)) > 0 and not jogo.game_over(jogo.tabuleiro): #loop principal do jogo
    if primeiro_movimento:
        jogo.vez_bot()
        primeiro_movimento = ''

    jogo.vez_humano()
    jogo.vez_bot()

if jogo.wins(jogo.tabuleiro, jogo.HUMANO):
    print(f'Sua vez[{jogo.humano_escolha}]')
    jogo.mostra_tabuleiro(jogo.tabuleiro)
    print('Você ganhou, aff...')

elif jogo.wins(jogo.tabuleiro, jogo.BOT):
    print(f'Minha vez! Deixe eu pensar... [{jogo.bot_escolha}]')
    jogo.mostra_tabuleiro(jogo.tabuleiro)
    print('Perdeste! Hahah')

else:
    jogo.mostra_tabuleiro(jogo.tabuleiro)
    print('Ih, deu velha...')

exit()
