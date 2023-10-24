import random

# List of the cards
cards_list = {"\u2663": [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
              "\u2665": [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
              "\u2666": [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
              "\u2660": [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
              }
stop_game = False
lost = False
sum_own_cards = 0
sum_opponent_cards = 0


# def for deal
def deal(sum_cards):
    # Choose a random card type then a random card
    card_type = random.choice(list(cards_list.keys()))
    card = random.choice(cards_list[card_type])
    # Remove the card from the deck
    cards_list[card_type].remove(card)
    # Check the value of ace card
    if card == 11:
        if sum_cards + 11 > 21:
            card = 1
    return card_type, card


# Printing text in different deal
# Need the card type the card number to print these values
# Need number_of_deal to know which turn is it
# Sum_cards: This parameter contains the values of the cards
# if this equal to 0 then we don't count with this
# blnOpponent_card is a boolean
# We check with this parameter whose turn it is
def print_result(card_type, card_number, number_of_deal, sum_cards=0, blnOpponent_card=False):
    import time

    list_of_deals = ["first", "second", "third", "forth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth",
                     "eleventh"]
    if sum_cards == 0:
        if not blnOpponent_card:
            print(f"Your {list_of_deals[number_of_deal]} card: {card_type}, {card_number}\n")
        else:
            print(f"Your opponent's {list_of_deals[number_of_deal]} card: {card_type}, {card_number}\n")
    else:
        if not blnOpponent_card:
            print(f"Your {list_of_deals[number_of_deal]} card: {card_type}, {card_number}\nSum: {sum_cards}\n")
        else:
            print(
                f"Your opponent's {list_of_deals[number_of_deal]} card: {card_type}, {card_number}\nSum: {sum_cards}\n")

    time.sleep(1)  # Wait for 1 sec


own_cards = []
opponent_cards = []

# First deal for ourselves
own_cards.append(deal(sum_own_cards))
print_result(own_cards[0][0], own_cards[0][1], 0, 0, False)
# First deal for opponent
opponent_cards.append(deal(sum_opponent_cards))
print_result(opponent_cards[0][0], opponent_cards[0][1], 0, 0, True)
# Second deal for ourselves
own_cards.append(deal(sum_own_cards))
sum_own_cards = own_cards[0][1] + own_cards[1][1]
print_result(own_cards[1][0], own_cards[1][1], 1, sum_own_cards, False)
# Second (hidden) deal for opponent
# Don't show opponent's second until we end our turns
opponent_cards.append(deal(sum_opponent_cards))
sum_opponent_cards = opponent_cards[0][1] + opponent_cards[1][1]
# Need a variable to store the turn of deals and use it for the print result function
deal_turn = 2
# We play until we say no or lost become true (when our cards values more then 21)
while not stop_game and lost == False:
    answer = ""
    # The answer must be yes or no
    while answer != "yes" and answer != "no":
        answer = input("Type yes if you want one more card else type no:\n").lower()
        if answer.lower() == "no":
            stop_game = True
        elif answer.lower() == "yes":
            own_cards.append(deal(sum_own_cards))
            sum_own_cards = sum_own_cards + own_cards[deal_turn][1]
            print_result(own_cards[deal_turn][0], own_cards[deal_turn][1], deal_turn, sum_own_cards, False)
            deal_turn += 1
            if sum_own_cards > 21:
                lost = True
deal_turn = 1
# if we stopped the game and the sum of our cards values aren't bigger then 21 the opponent's turn begin:
if not lost:
    while sum_opponent_cards < 17:
        print_result(opponent_cards[deal_turn][0], opponent_cards[deal_turn][1], 1, sum_opponent_cards, True)
        opponent_cards.append(deal(sum_opponent_cards))
        sum_opponent_cards = sum_opponent_cards + opponent_cards[deal_turn][1]
        deal_turn += 1

    print_result(opponent_cards[deal_turn][0], opponent_cards[deal_turn][1], 1, sum_opponent_cards, True)

# Print the game result
if lost:
    print("The sum of your cards exceeded 21. You loose!")
else:
    print(f"The sum of your cards: {sum_own_cards}\nThe sum of your opponent cards: {sum_opponent_cards}")
    if sum_own_cards > sum_opponent_cards:
        print("You win!")
    elif sum_own_cards == sum_opponent_cards:
        print("Draw!")
    else:
        if sum_opponent_cards > 21:
            print("The sum of your opponents cards exceeded 21. You win!")
        else:
            print("You loose!")
