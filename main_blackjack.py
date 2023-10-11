import random

cards_list = {"heart": [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
              "tiles": [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
              "pikes": [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
              "clover": [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
              }
stop_game = False
sum_own_cards = 0
sum_opponent_cards = 0


def deal(sum_cards):
    card_type = random.choice(list(cards_list.keys()))
    card = random.choice(cards_list[card_type])
    if card == 11:
        # if sum_cards + 11 > 21:
        card = 1
        print("Itt a card")

    cards_list[card_type].remove(card)
    return card_type, card


def print_result(card_type, card_number, number_of_deal, sum_cards=0, blnOpponent_card=False):
    list_of_deal = ["first", "second", "third", "forth", "fifth", "sixth", "seventh", "egihth", "ninth", "tenth",
                    "eleventh"]
    if sum_cards == 0:
        if not blnOpponent_card:
            return print(f"Your {list_of_deal[number_of_deal]} card: {card_type}, {card_number}\n")
        else:
            return print(f"Your opponent's {list_of_deal[number_of_deal]} card: {card_type}, {card_number}\n")
    else:
        if not blnOpponent_card:
            return print(f"Your {list_of_deal[number_of_deal]} card: {card_type}, {card_number}\nSum: {sum_cards}\n")
        else:
            return print(
                f"Your opponent's {list_of_deal[number_of_deal]} card: {card_type}, {card_number}\nSum: {sum_cards}\n")


own_cards = []
opponent_cards = []

# Első deal magunknak
own_cards.append(deal(sum_own_cards))
print_result(own_cards[0][0], own_cards[0][1], 0, 0, False)
# Első deal ellenfélnek
opponent_cards.append(deal(sum_opponent_cards))
print_result(opponent_cards[0][0], opponent_cards[0][1], 0, 0, True)
# Második deal magunknak
own_cards.append(deal(sum_own_cards))
sum_own_cards = own_cards[0][1] + own_cards[1][1]
print_result(own_cards[1][0], own_cards[1][1], 1, sum_own_cards, False)
# Második (rejtett) deal az elenfélnek
opponent_cards.append(deal(sum_opponent_cards))
sum_opponent_cards = opponent_cards[0][1] + opponent_cards[1][1]
deal_turn = 2
while not stop_game:
    answer = ""
    while answer != "yes" and answer != "no":
        answer = input("Type yes if you want one more card else type no:\n").lower()
        own_cards.append(deal(sum_own_cards))
        if answer.lower() == "yes":

            sum_own_cards = sum_own_cards + own_cards[deal_turn][1]
            print_result(own_cards[deal_turn][0], own_cards[deal_turn][1], deal_turn, sum_own_cards, False)
            deal_turn += 1
            # if sum_own_cards > 21:
            #     stop_game = True
        elif answer.lower() == "no":
            print_result(opponent_cards[1][0], opponent_cards[1][1], 1, sum_opponent_cards, True)
            stop_game = True
    # stop_game = True
