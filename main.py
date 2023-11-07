"""
     JA rzucam kartę i automatycznie dobiera mi kolejną ze stosiku
     rusza mój pionek 
     karta wpada do stosiku i stosik jest tasowany
"""

from board import Board
from cards import Deck
from menu import Menu

menu = Menu()
how_many_players_in_this_game_result = menu.how_many_players_in_this_game()

deck = Deck(how_many_players_in_this_game_result)
hands_and_pile = deck.map_players_colors()

print(hands_and_pile)
board = Board(how_many_players_in_this_game_result)
board.board_moving()

# pamiętać o tym, że to jest set i wartości wewnatrz są unikatowe, zatem jak będzie 2 razy Kamil to tylko raz rozda karty
# teraz doprowadzić do sytuacji w której gracz może, rzucać tylko karty, któe m w ręce
# następnie popracować nad tym jak mają się zachowywać boty
