class Menu:

    def __init__(self, player='Player'):
        self.player = player
        self.presenter = 'Ross'

    def __str__(self):
        pass

    def introduce(self):
        print(
            f'Hi {self.player} My name is {self.presenter}.')
    
    def how_many_players_in_this_game (self):
        number_of_players = int(input('Ilu graczy ma być w tym meczu? '))
        human_players = []
        x = 0
        while x < number_of_players:
            name = input('Podaj swoje imię: ')
            human_players.append(name)
            x += 1         
        return human_players