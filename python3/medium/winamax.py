import sys

cards_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13,
              "A": 14}

n = int(input())  # the number of cards for player 1
p1_cards = [cards_dict[input()[0:-1]] for i in range(n)]
m = int(input())  # the number of cards for player 2
p2_cards = [cards_dict[input()[0:-1]] for j in range(m)]

counter = 0
while True:
    try:
        p1_curr_cards, p2_curr_cards = [p1_cards.pop(0)], [p2_cards.pop(0)]
    except IndexError:
        print("1",counter) if len(p1_cards) > 0 else print("2",counter)
        break

    counter += 1

    try:
        while p1_curr_cards[-1] == p2_curr_cards[-1]:
            for _ in range(4):
                p1_curr_cards.append(p1_cards.pop(0))
                p2_curr_cards.append(p2_cards.pop(0))
    except IndexError:
        print("PAT")
        break

    if p1_curr_cards[-1] > p2_curr_cards[-1]:
        p1_cards += p1_curr_cards + p2_curr_cards
    else:
        p2_cards += p1_curr_cards + p2_curr_cards








