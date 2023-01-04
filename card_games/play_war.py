from basics.deck import Deck
from basics.player import Player
# TODO: rename basics dir to 'src'

jay = Player('Jay')
julie = Player('Julie')

deck = Deck()

# Distribute cards
while len(deck.draw_pile):
    for player in [jay, julie]:
        deck.draw_card(player)

# play turn
while jay.has_cards() and julie.has_cards():
    print(f"\nCards: {jay.name} has {len(jay.hand)}, {julie.name} has {len(julie.hand)}")
    jay.play_card()
    julie.play_card()
    print(f"{jay.last_played_card()} vs. {julie.last_played_card()}")
    if jay.last_played_card().value > julie.last_played_card().value:
        print("Jay wins")
        jay.pick_up_cards()
        jay.take_played_cards(julie)
    elif jay.last_played_card().value < julie.last_played_card().value:
        print("Julie wins")
        julie.pick_up_cards()
        julie.take_played_cards(jay)
    else:
        print("War!")
        for x in range(0,3):
            if not jay.has_cards() or not julie.has_cards():
                print("No more cards! Need to handle this edge case")
                break
            print("Playing card...")
            julie.play_card()
            jay.play_card()
        print(f"There are now {len(jay.played_cards) + len(julie.played_cards)} cards up for grabs. Go!")

if len(jay.played_cards) > 0:
    print("No more cards! This is an edge case!")

# TODO: edge case - last cards were played down during war
# Ends with 8 cards up for grabs, no cards left to play
# player.has_cards() is False so loop ends

print("\nFINAL SCORE!")
julie.print_hand_length()
jay.print_hand_length()
