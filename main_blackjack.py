import random

cards_list = {"heart": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11],
              "tiles": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11],
              "pikes": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11],
              "clover": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11],
              }


def deal():
    card_type = random.choice(list(cards_list.keys()))
    card = random.choice(cards_list[card_type])
    cards_list[card_type].remove(card)
    return card_type, card


print(f"Your cards: {deal()[0]}, {deal()[1]}")

# end_game = False
# while not end_game:


# print(cards_list)
