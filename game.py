from cards import Deck


class Game:
    def __init__(self):
        self.deck = Deck()                                  # Inicjalizacja talii kart
        self.players, self.pile = self.deck.deal_cards()    # Rozdanie kart graczom
        self.player_turn = 0  # Numer gracza, który jest aktualnie na ruchu

    def play_card(self, player_name, card):
        # Sprawdź, czy to jest tura gracza
        current_player = self.players[self.player_turn]
        if current_player[0] != player_name:
            print("Nie jest twoją turą!")
            return

            # Sprawdź, czy gracz ma tę kartę
        if card not in current_player:
            print("Nie masz tej karty w ręce!")
            return

        # Wykonaj ruch pionkiem (tu może być implementacja w przyszłości)

        # Usuń kartę z ręki gracza
        current_player.remove(card)

        # Dodaj kartę z pile do ręki gracza
        new_card = self.pile.pop(0)
        current_player.append(new_card)

        # Dodaj wykorzystaną kartę z powrotem do pile
        self.pile.append(card)

        # Tasuj pile
        self.deck.shuffle_pile(self.pile)

        # Przełącz do następnego gracza
        self.player_turn = (self.player_turn + 1) % len(self.players)
