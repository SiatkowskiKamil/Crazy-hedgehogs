from menu import Menu


class Board:
    def __init__(self, player_info):
        self.board_size = 10
        self.player_info = player_info

    def board_moving(self):
        players = self.player_info
        player_values = {player: 1 for player in players.keys()}

        print(player_values)

        while True:

            card = input("Podaj kartę: ")

            if card == 'multi ++':
                color = input("What color? ")
                player_values[color] += 2
                if player_values[color] >= 10:
                    print(f"Player {color} Win!")
                    break

            elif card == 'multi +':
                color = input("What color? ")
                player_values[color] += 1
                if player_values[color] >= 10:
                    print(f"Player {color} Win!")
                    break

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
                    if player_values[min_color] >= 10:
                        print(f"Player {min_color} Win!")
                        break

            elif card == 'multi >':
                if player_values:
                    min_color = min(player_values, key=player_values.get)
                    player_values[min_color] += 1
                    if player_values[min_color] >= 10:
                        print(f"Player {min_color} Win!")
                        break

            elif card[-2:] == '++':
                player_values[card[:-3]] += 2
                if player_values[card[:-3]] >= 10:
                    print(f"Player {card[:-3]} Win!")
                    break

            elif card[-1:] == '+':
                player_values[card[:-2]] += 1
                if player_values[card[:-2]] >= 10:
                    print(f"Player {card[:-2]} Win!")
                    break

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