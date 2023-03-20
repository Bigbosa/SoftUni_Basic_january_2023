travel = float(input())

number_of_puzzles = int(input())
talking_dolls = int(input())
number_of_tedi_bears = int(input())
number_of_minions = int(input())
number_truck = int(input())

puzzle = 2.60
dolls = 3
tedi_bears = 4.10
minions = 8.20
truck = 2

price = number_of_puzzles \
        + talking_dolls \
        + number_of_tedi_bears \
        + number_of_minions \
        + number_truck

price_2 = (number_of_puzzles * puzzle)  \
          + (talking_dolls * dolls) \
          + (number_of_tedi_bears * tedi_bears) \
          + (number_of_minions * minions) \
          + (number_truck * truck)

if price >= 50:
    price_2 *= 0.75

price_2 *= 0.90

if price_2 >= travel:
    print(f"Yes! {price_2 - travel:.2f} lv left.")
else:
    print(f"Not enough money! {travel - price_2:.2f} lv needed.")


