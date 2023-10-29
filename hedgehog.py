import random
from menu import Menu


class Hedgehog:
    def __init__(self):
        pass

    def display_players(self):
        hedgehog_colors = ['yellow', 'red', 'green', 'blue', 'purple']
        players = ['Rachel', 'Monica', 'Phoebe', 'Joey', 'Chandler']

        random.shuffle(hedgehog_colors)
        random.shuffle(players)
        
        pairs = {color: player for color, 
                 player in zip(hedgehog_colors, players)}
        
        human_players = Menu().how_many_players_in_this_game()
        for colors in pairs:
            if human_players:
                new_name = human_players.pop(0)
                pairs[colors] = new_name
        
        return pairs