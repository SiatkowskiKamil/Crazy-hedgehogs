import random
from userManager import UserLoginClass


class Menu:

    def __init__(self, player='Player'):
        self.player = player
        self.presenter = 'Ross'
        self.user_login = UserLoginClass()

    def __str__(self):
        pass

    def introduce(self):
        print(
            f'Hi {self.player} My name is {self.presenter}.')

    def user_logging(self, username_input, password_input):
        self.user_login.login(username_input, password_input)

    def how_many_players_in_this_game(self):
        number_of_players = int(input('Ilu graczy ma być w tym meczu? '))
        human_players = []

        if self.user_login.log:
            human_players.append(self.user_login.current_username)
            x = 1
            while x < number_of_players:
                name = input('Podaj imię kolejnego gracza: ')
                human_players.append(name)
                x += 1
        else:
            x = 1
            human_players.append("Gość")
            while x < number_of_players:
                name = input('Podaj imię kolejnego gracza: ')
                human_players.append(name)
                x += 1

        hedgehog_colors = ['yellow', 'red', 'green', 'blue', 'purple']
        players = ['Rachel', 'Monica', 'Phoebe', 'Joey', 'Chandler']

        while len(human_players) < 5:
            if len(players) > 0:
                human_players.append(players.pop(0))

        random.shuffle(hedgehog_colors)
        random.shuffle(human_players)

        pairs = {color: player for color, player in zip(hedgehog_colors, human_players)}

        return pairs
