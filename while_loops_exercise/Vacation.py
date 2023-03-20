money_for_exursion = float(input())
all_money = float(input())
day_counter = 0
spend_counter = 0

while all_money < money_for_exursion and  spend_counter < 5:
    command = input()
    money = float(input())
    day_counter += 1

    if command == "save":
        all_money += money
        spend_counter = 0
    elif command == "spend":
        all_money -= money
        spend_counter += 1
    if all_money <0:
        all_money = 0

if spend_counter == 5:
    print("You can't save the money.")
    print(day_counter)

if all_money >= money_for_exursion:
    print(f"You saved the money for {day_counter} days.")
