"""
    Co musze zrobić?
    Stworzyć klasę Menu, któa będzie wyświetlała tekst powitalny i opcje do wyboru

    jeżeli przesyłam gracza (minimum jednego) to do 5 graczy dobiera BOTY,
    stworzyć listę imion botów aby nie były to player 1 itd
     Mamy wybraną 5 graczy, więc każdemu losuje karty i resztę na stosik
     jak rzucam kartę z ręki to dobiera mi pierwszą ze stosiku
     moje rzucone idą na stosik zużytych
     jak kończy mi się stosik to biorę stosik zużytych i stoisk = stosik zużytych.shuffle


     JA rzucam kartę i automatycznie dobiera mi kolejną ze stosiku
     rusza mój pionek 
     karta wpada do stosiku i stosik jest tasowany
"""


from hedgehog import Hedgehog
from cards import Deck

deck = Deck()

result = deck.map_players_colors()

for key, value in result.items():
    if "'s hand" in key:
        print(f"{key}: {', '.join(value)}")
    else:
        print(f"{key}: {value}")

players, pile = deck.deal_cards()
print(f'Pile: {pile}')
