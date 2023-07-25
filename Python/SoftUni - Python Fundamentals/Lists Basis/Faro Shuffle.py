deck = input().split()
shuffles = int(input())

for shuffle in range(shuffles):
    final_deck = []
    middle = len(deck) // 2
    deck_1 = deck[0:middle]
    deck_2 = deck[middle:]
    for card_index in range(len(deck_1)):
        final_deck.append(deck_1[card_index])
        final_deck.append(deck_2[card_index])

    deck = final_deck

print(deck)

