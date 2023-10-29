import random
from hedgehog import Hedgehog


class Deck:
    def __init__(self):
        self.cards = [
            'yellow ++', 'red ++', 'green ++', 'blue ++', 'purple ++',
            'yellow ++', 'red ++', 'green ++', 'blue ++', 'purple ++',
            'yellow +', 'red +', 'green +', 'blue +', 'purple +',
            'yellow +', 'red +', 'green +', 'blue +', 'purple +',
            'yellow +', 'red +', 'green +', 'blue +', 'purple +',
            'yellow +', 'red +', 'green +', 'blue +', 'purple +',
            'yellow +', 'red +', 'green +', 'blue +', 'purple +',
            'yellow -', 'red -', 'green -', 'blue -', 'purple -',
            'yellow -', 'red -', 'green -', 'blue -', 'purple -',
            'yellow +', 'red +', 'green +', 'blue +', 'purple +',
            'yellow +', 'red +', 'green +', 'blue +', 'purple +',
            'yellow +', 'red +', 'green +', 'blue +', 'purple +',
            'yellow +', 'red +', 'green +', 'blue +', 'purple +',
            'yellow +', 'red +', 'green +', 'blue +', 'purple +',
            'yellow -', 'red -', 'green -', 'blue -', 'purple -',
            'yellow -', 'red -', 'green -', 'blue -', 'purple -',
            'multi >>', 'multi >>',
            'multi >>', 'multi >>',
            'multi >', 'multi >', 'multi >',
            'multi >', 'multi >', 'multi >',
            'multi +', 'multi +', 'multi +', 'multi +', 'multi +',
            'multi +', 'multi +', 'multi +', 'multi +', 'multi +',
            'multi -', 'multi -',
            'multi -', 'multi -',
        ]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_cards(self):
        self.shuffle()

        players = []
        pile = []

        for _ in range(5):
            player_hand = []
            for _ in range(5):
                card = self.cards.pop()
                player_hand.append(card)
            players.append(player_hand)

        pile = self.cards

        return players, pile

    def map_players_colors(self):
        class_A_result = Hedgehog().display_players()
        mapped_result = {}

        for i, player_hand in enumerate(self.deal_cards()[0], 1):
            player_name = list(class_A_result.values())[i - 1]
            color = list(class_A_result.keys())[i - 1]
            mapped_result[f"{player_name}'s hand"] = player_hand
            mapped_result[f"{player_name}'s color"] = color

        return mapped_result
