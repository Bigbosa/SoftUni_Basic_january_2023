saved_money = 0

while True:
    destination = input()

    if destination == "End":
        break

    minimal_budget = float(input())
    saved_money = 0

    while saved_money < minimal_budget:
        saved = float(input())
        saved_money += saved

    print(f"Going to {destination}!")


