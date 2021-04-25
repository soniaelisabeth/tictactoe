from random import choice
from math import inf

class JogodaVelha():

    #variaveis globais
    tabuleiro = [ 
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
    HUMANO = -1
    BOT = +1

    def __init__(self, humano_escolha, bot_escolha, dificuldade):
        self.humano_escolha = humano_escolha
        self.bot_escolha = bot_escolha
        self.dificuldade = dificuldade
    
    def mostra_tabuleiro(self,state): #mostra o tabuleiro atual
        chars = {
            -1: self.humano_escolha,
            +1: self.bot_escolha,
            0: '_'}
        str_line = '---------------'

        print('\n' + str_line)
        for row in state:
            for celula in row:
                symbol = chars[celula]
                print(f'[ {symbol} ]', end='')
            print('\n' + str_line)

    def jogada(self,x, y, player): #faz uma jogada
        if self.jogada_valida(x, y):
            self.tabuleiro[x][y] = player
            return True
        else:
            return False

    def jogada_valida(self,x, y): #analisa para verificar se a jogada é válida
        if [x, y] in self.celulas_vazias(self.tabuleiro):
            return True
        else:
            return False

    def celulas_vazias(self,state): #analisa quais as partes do tabuleiro estão vagas
        celulas = []
        for x, row in enumerate(state):
            for y, celula in enumerate(row):
                if celula == 0:
                    celulas.append([x, y])

        return celulas

    def vez_humano(self): # faz jogada do humano
        profundidade = len(self.celulas_vazias(self.tabuleiro))
        if profundidade == 0 or self.game_over(self.tabuleiro):
            return

        move = -1
        moves = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
        }

        print(f'Sua vez: [{self.humano_escolha}]')
        self.mostra_tabuleiro(self.tabuleiro)

        while move < 1 or move > 9:
            try:
                move = int(input('Use os números: (1-9): '))
                coord = moves[move]
                can_move = self.jogada(coord[0], coord[1], self.HUMANO)

                if not can_move:
                    print('Movimento inválido D:')
                    move = -1
            except (KeyError, ValueError):
                print('Tente novamente!')


    def vez_bot(self): # realiza a jogada do bot
        level_profund = ''
        profundidade = len(self.celulas_vazias(self.tabuleiro))
        if profundidade == 0 or self.game_over(self.tabuleiro):
            return
        
        print(f'Minha vez... [{self.bot_escolha}]')
            
        if profundidade == 9 or self.dificuldade == '1': 
            x = choice([0, 1, 2]) # escolhe numero randomico para dificuldade mais baixa
            y = choice([0, 1, 2])
        else:
            if self.dificuldade == '2':
                level_profund = 4
            if self.dificuldade == '3': #quanto maior a analise de profundidade, mais inteligente o bot será
                level_profund = 9
            new_profundidade = profundidade - level_profund
            move = self.minimax(self.tabuleiro, new_profundidade, self.BOT)
            x, y = move[0], move[1]

        self.jogada(x, y, self.BOT)

    def minimax(self, state, profundidade, player): #algoritmo minimax para análise das jogadas
        if player == self.BOT:
            best = [-1, -1, -inf]
        else:
            best = [-1, -1, +inf]

        if profundidade == 0 or self.game_over(state):
            score = self.avaliacao(state)
            return [-1, -1, score]

        for celula in self.celulas_vazias(state):
            x, y = celula[0], celula[1]
            state[x][y] = player
            score = self.minimax(state, profundidade, -player) # diminui profundidade para ajuste de níveis
            state[x][y] = 0
            score[0], score[1] = x, y

            if player == self.BOT:
                if score[2] > best[2]:
                    best = score 
            else:
                if score[2] < best[2]:
                    best = score 

        return best
    
    def avaliacao(self,state): #avalia o score
        if self.wins(state, self.BOT):
            score = +1
        elif self.wins(state, self.HUMANO):
            score = -1
        else:
            score = 0

        return score

    def wins(self,state, player): #analisa estado vencedor
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

    def game_over(self,state): #estado de fim de jogo
        return self.wins(state, self.HUMANO) or self.wins(state, self.BOT)