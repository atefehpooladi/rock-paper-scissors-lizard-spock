import random
import matplotlib.pyplot as plt


class Player:

    signs = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    def __init__(self, player_name, player_move):
        self.player_name = player_name

        if player_move in self.signs:
            self.player_move = player_move
        else:
            sign = ''
            while sign not in self.signs:
                for option in self.signs:
                    print(option)
                sign = input('please choose from the above options:')
            self.player_move = sign


def compare_moves(player_move1, player_move2):

    if player_move1 == 'scissors' and (player_move2 == 'paper' or player_move2 == 'lizard'):
        return True
    if player_move1 == 'paper' and (player_move2 == 'rock' or player_move2 == 'spock'):
        return True
    if player_move1 == 'rock' and (player_move2 == 'lizard' or player_move2 == 'scissors'):
        return True
    if player_move1 == 'lizard' and (player_move2 == 'spock' or player_move2 == 'paper'):
        return True
    if player_move1 == 'spock' and (player_move2 == 'scissors' or player_move2 == 'rock'):
        return True
    return False


def two_player_game(player1, sign1, player2, sign2):

    if sign1 == sign2:
        player_input = int(input('{} have to choice 0: Heads or 1: Tails'.format(player1)))
        random_coin = random.randint(0, 1)
        if player_input == random_coin:
            allPlayer.pop(player2)
            print('winner is :', player1 + '\n')
            for name in allPlayer.keys():
                if name != player1:
                    print(name + ',', end=' ')
            return player1, sign1
        else:
            allPlayer.pop(player1)
            print('winner is :', player2 + '\n')
            for name in allPlayer.keys():
                if name != player2:
                    print(name + ',', end=' ')
            return player2, sign2
    elif compare_moves(sign1, sign2):
        allPlayer.pop(player2)
        print('winner is :', player1 + '\n')
        for name in allPlayer.keys():
            if name != player1:
                print(name+',', end=' ')
    else:
        allPlayer.pop(player1)
        print('winner is :', player2 + '\n')
        for name in allPlayer.keys():
            if name != player2:
                print(name+',', end=' ')
        return player2, sign2


def barchart(input_sign):

    dict_signs = {}
    for x in Player.signs:
        for y in input_sign:
            if y in x:
                try:
                    dict_signs[x] += 1
                except KeyError:
                    dict_signs[x] = 1
            else:
                dict_signs[x] = dict_signs.get(x, 0)
    print(dict_signs)
    names = list(dict_signs.keys())
    values = list(dict_signs.values())
    plt.bar(range(len(dict_signs)), values, tick_label=names)
    plt.show()
    plt.savefig('bar.png')


if __name__ == '__main__':

    allPlayer = {}
    countOfPlayer = int(input("How many players? "))
    for i in range(countOfPlayer):
        p = Player(input("Name: "), input("Move: "))
        allPlayer.update({p.player_name: p.player_move})
    all_selected_sign = allPlayer.copy()
    while len(allPlayer) != 1:
        for i in range(int(len(allPlayer)/2)):
            if(len(allPlayer)) <= 2:
                print('final ')
            else:
                print('round ', i + 1)
            key = list(allPlayer.keys())
            value = list(allPlayer.values())
            two_player_game(key[i], value[i], key[i+1], value[i+1])
            print('\n'+'--------------------------------------------')

    barchart(list(all_selected_sign.values()))
