from random import choice
from math import inf

class JogodaVelha():
    HUMANO = -1
    BOT = +1
    tabuleiro = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

    def __init__(self, humano_escolha, bot_escolha, dificuldade):
        self.humano_escolha = humano_escolha
        self.bot_escolha = bot_escolha
        self.dificuldade = dificuldade


    def avaliacao(self,state):
        if wins(state, self.BOT):
            score = +1
        elif wins(state, self.HUMANO):
            score = -1
        else:
            score = 0

        return score


    def wins(self,state, player):
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


    def game_over(self,state):
        return wins(state, self.HUMANO) or wins(state, self.BOT)


    def celulas_vazias(self,state):
        celulas = []
        for x, row in enumerate(state):
            for y, celula in enumerate(row):
                if celula == 0:
                    celulas.append([x, y])

        return celulas


    def jogada_valida(self,x, y):
        if [x, y] in celulas_vazias(tabuleiro):
            return True
        else:
            return False


    def jogada(self,x, y, player):
        if jogada_valida(x, y):
            tabuleiro[x][y] = player
            return True
        else:
            return False

    def mostra_tabuleiro(self,state, bot_escolha, humano_escolha):
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


    def vez_bot(self,bot_escolha, humano_escolha, dificuldade):
        level_profund = ''
        profundidade = len(celulas_vazias(tabuleiro))
        if profundidade == 0 or game_over(tabuleiro):
            return
        
        print(f'Minha vez... [{bot_escolha}]')
            
        if profundidade == 9 or dificuldade == '1': 
            x = choice([0, 1, 2]) #numero randomico para dificuldade mais baixa
            y = choice([0, 1, 2])
        else:
            if dificuldade == '2':
                level_profund = 4
            if dificuldade == '3': #quanto maior a profundidade, mais inteligente
                level_profund = 8
            new_profundidade = profundidade - level_profund
            move = minimax(tabuleiro, new_profundidade, self.BOT)
            x, y = move[0], move[1]

        jogada(x, y, self.BOT)

    def minimax(self, state, profundidade, player):
        if player == self.BOT:
            best = [-1, -1, -inf]
        else:
            best = [-1, -1, +inf]

        if profundidade == 0 or game_over(state):
            score = avaliacao(state)
            return [-1, -1, score]

        for celula in celulas_vazias(state):
            x, y = celula[0], celula[1]
            state[x][y] = player
            score = minimax(state, profundidade, -player) # diminuir profund
            state[x][y] = 0
            score[0], score[1] = x, y

            if player == self.BOT:
                if score[2] > best[2]:
                    best = score 
            else:
                if score[2] < best[2]:
                    best = score 

        return best


    def vez_humano(self, bot_escolha, humano_escolha):
        profundidade = len(celulas_vazias(tabuleiro))
        if profundidade == 0 or game_over(tabuleiro):
            return

        move = -1
        moves = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
        }

        print(f'Sua vez: [{humano_escolha}]')
        mostra_tabuleiro(tabuleiro, bot_escolha, humano_escolha)

        while move < 1 or move > 9:
            try:
                move = int(input('Use os números: (1-9): '))
                coord = moves[move]
                can_move = jogada(coord[0], coord[1], self.HUMANO)

                if not can_move:
                    print('Movimento inválido D:')
                    move = -1
            except (EOFError, KeytabuleiroInterrupt):
                print('Byeeeeee')
                exit()
            except (KeyError, ValueError):
                print('Tente novamente!')