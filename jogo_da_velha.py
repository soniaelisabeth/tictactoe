from random import choice
from math import inf

HUMANO = -1
BOT = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]


def avaliacao(state):
    if wins(state, BOT):
        score = +1
    elif wins(state, HUMANO):
        score = -1
    else:
        score = 0

    return score


def wins(state, player):
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def game_over(state):
    return wins(state, HUMANO) or wins(state, BOT)


def celulas_vazias(state):
    celulas = []
    for x, row in enumerate(state):
        for y, celula in enumerate(row):
            if celula == 0:
                celulas.append([x, y])

    return celulas


def jogada_valida(x, y):
    if [x, y] in celulas_vazias(board):
        return True
    else:
        return False


def jogada(x, y, player):
    if jogada_valida(x, y):
        board[x][y] = player
        return True
    else:
        return False


def mostra_board(state, bot_escolha, humano_escolha):
    chars = {
        -1: humano_escolha,
        +1: bot_escolha,
        0: '_'}
    str_line = '---------------'

    print('\n' + str_line)
    for row in state:
        for celula in row:
            symbol = chars[celula]
            print(f'[ {symbol} ]', end='')
        print('\n' + str_line)


def vez_bot(bot_escolha, humano_escolha, dificuldade):
    level_profund = ''
    depth = len(celulas_vazias(board))
    if depth == 0 or game_over(board):
        return
    
    print(f'Minha vez... [{bot_escolha}]')
        
    if depth == 9 or dificuldade == '1': 
        x = choice([0, 1, 2]) #numero randomico
        y = choice([0, 1, 2])
    else:
        if dificuldade == '2':
            level_profund = 4
        if dificuldade == '3': #quanto maior a profundidade, mais inteligente
            level_profund = 8
        new_depth = depth - level_profund
        move = minimax(board, new_depth, BOT)
        x, y = move[0], move[1]

    jogada(x, y, BOT)

def minimax(state, depth, player):
    if player == BOT:
        best = [-1, -1, -inf]
    else:
        best = [-1, -1, +inf]

    if depth == 0 or game_over(state):
        score = avaliacao(state)
        return [-1, -1, score]

    for celula in celulas_vazias(state):
        x, y = celula[0], celula[1]
        state[x][y] = player
        score = minimax(state, depth, -player) # diminuir profund
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == BOT:
            if score[2] > best[2]:
                best = score 
        else:
            if score[2] < best[2]:
                best = score 

    return best


def vez_humano(bot_escolha, humano_escolha):
    depth = len(celulas_vazias(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    print(f'Sua vez: [{humano_escolha}]')
    mostra_board(board, bot_escolha, humano_escolha)

    while move < 1 or move > 9:
        try:
            move = int(input('Use os números: (1-9): '))
            coord = moves[move]
            can_move = jogada(coord[0], coord[1], HUMANO)

            if not can_move:
                print('Movimento inválido D:')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Byeeeeee')
            exit()
        except (KeyError, ValueError):
            print('Tente novamente!')


def main():
    humano_escolha, bot_escolha, dificuldade = '','','',

    while humano_escolha != 'O' and humano_escolha != 'X':
        try:
            print('')
            print('Bem vindo ao jogo da velha, professor Allan!')
            humano_escolha = input('Escolha X or O: ').upper()
        except (EOFError, KeyboardInterrupt):
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
        except (EOFError, KeyboardInterrupt):
            print('Byeeeee')
            exit()
        except (KeyError, ValueError):
            print('Tente novamente!')

    primeiro_movimento = 'H'
    while len(celulas_vazias(board)) > 0 and not game_over(board):
        if primeiro_movimento:
            vez_bot(bot_escolha, humano_escolha, dificuldade)
            primeiro_movimento = ''

        vez_humano(bot_escolha, humano_escolha)
        vez_bot(bot_escolha, humano_escolha, dificuldade)

    if wins(board, HUMANO):

        print(f'Sua vez[{humano_escolha}]')
        mostra_board(board, bot_escolha, humano_escolha)
        print('Você ganhou, aff...')
    elif wins(board, BOT):

        print(f'Minha vez! Deixe eu pensar... [{bot_escolha}]')
        mostra_board(board, bot_escolha, humano_escolha)
        print('Perdeste! Hahah')
    else:

        mostra_board(board, bot_escolha, humano_escolha)
        print('Ih, deu velha...')

    exit()


if __name__ == '__main__':
    main()