number = int(input()) * 750

total = 0
vero_need = 0
plots = 0
plates = 0



text = input()

while text != "End":
    number_dishes = int(text)
    if number_dishes == int(text):
        total += 1

    if total % 3 == 0:
        plots += number_dishes
        vero_need += number_dishes * 15

    else:
        plates += number_dishes
        vero_need += number_dishes * 5

    if vero_need > number:
        break

    text = input()

diff = abs(number - vero_need)
if vero_need <= number:
    print("Detergent was enough!")
    print(f"{plates} dishes and {plots} pots were washed.")
    print(f"Leftover detergent {diff} ml.")
else:
    print(f"Not enough detergent, {diff} ml. more necessary!")
