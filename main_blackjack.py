import random

cards_list = {"heart": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11],
              "tiles": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11],
              "pikes": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11],
              "clover": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11],
              }
stop_game = False


def deal():
    card_type = random.choice(list(cards_list.keys()))
    card = random.choice(cards_list[card_type])
    cards_list[card_type].remove(card)
    return card_type, card


def print_result(card_type, card_number, number_of_deal, sum_cards=0, blnOpponent_card=False, blnSum=True):
    list_of_deal = ["first", "second", "third", "forth", "fifth", "sixth","seventh", "egihth", "ninth","tenth"]
    if not blnSum:
        if not blnOpponent_card:
            return print(f"Your {list_of_deal[number_of_deal]} card: {card_type}, {card_number}")
        else:
            return print(f"Your opponent's {list_of_deal[number_of_deal]} card: {card_type}, {card_number}")
    else:
        if not blnOpponent_card:
            return print(f"Your {list_of_deal[number_of_deal]} card: {card_type}, {card_number}\nSum: {sum_cards}")
        else:
            return print(f"Your opponent's {list_of_deal[number_of_deal]} card: {card_type}, {card_number}\nSum: {sum_cards}")


first_own_card = deal()
print_result(first_own_card[0], first_own_card[1],0,False,False,False)
#print(f"Your card: {first_own_card[0]}, {first_own_card[1]}")
print(f"Your opponent's card: {deal()[0]}, {deal()[1]}")
second_own_card = deal()
sum_own_card = first_own_card[1] + second_own_card[1]
print(f"Your second card: {second_own_card[0]}, {second_own_card[1]}\nSum: {sum_own_card}")
opponent_hidden_card = deal()
while not stop_game:
    answer = ""
    while answer != "yes" and answer != "no":
        answer = input("Type yes if you want one more card else type no:\n").lower()
    if answer.lower() == "yes":
        third_own_card = deal()
    stop_game = True
