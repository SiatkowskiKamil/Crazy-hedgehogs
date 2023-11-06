from hedgehog import Hedgehog


class Board:
    def __init__(self):
        self.board_size = 10

    def board_moving(self):
        players = Hedgehog().display_players()
        player_values = {player: 1 for player in players.keys()}

# 'yellow', 'purple', 'blue', 'red', 'green'

        while True:

            card = input("Podaj kartę: ")

            if card == 'multi ++':
                color = input("What color? ")
                player_values[color] += 2

            elif card == 'multi +':
                color = input("What color? ")
                player_values[color] += 1

            elif card == 'multi --':
                color = input("What color? ")
                player_values[color] -= 2
                if player_values[color] < 1:
                    player_values[color] = 1

            elif card == 'multi -':
                color = input("What color? ")
                player_values[color] -= 1
                if player_values[color] < 1:
                    player_values[color] = 1

            elif card == 'multi >>':
                if player_values:
                    min_color = min(player_values, key=player_values.get)
                    player_values[min_color] += 2

            elif card == 'multi >':
                if player_values:
                    min_color = min(player_values, key=player_values.get)
                    player_values[min_color] += 1

            elif card[-2:] == '++':
                player_values[card[:-3]] += 2

            elif card[-1:] == '+':
                player_values[card[:-2]] += 1

            elif card[-2:] == '--':
                player_values[card[:-3]] -= 2
                if player_values[card[:-3]] < 1:
                    player_values[card[:-3]] = 1

            elif card[-1:] == '-':
                player_values[card[:-2]] -= 1
                if player_values[card[:-2]] < 1:
                    player_values[card[:-2]] = 1

            else:
                print('break')
                break

            print(player_values)


board = Board()
board.board_moving()
