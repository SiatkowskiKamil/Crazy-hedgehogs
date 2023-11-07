import random


class Deck:
    def __init__(self, player_info):
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
            'multi -', 'multi -'
        ]
        self.player_info = player_info

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
        class_A_result = self.player_info
        mapped_result = {}

        for i, player_hand in enumerate(self.deal_cards()[0], 1):
            player_name = list(class_A_result.values())[i - 1]
            color = list(class_A_result.keys())[i - 1]
            mapped_result[f"{player_name}'s color"] = color
            mapped_result[f"{player_name}'s hand"] = player_hand

        for key, value in mapped_result.items():
            if "'s hand" in key:
                print(f"{key}: {', '.join(value)}")
            else:
                print(f"{key}: {value}")

        players, pile = self.deal_cards()
        print(f'Pile: {pile}')

        return mapped_result
