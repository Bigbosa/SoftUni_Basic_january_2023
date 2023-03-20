type_fuel = input()
quantity_fuel = float(input())
club_card = input()

price = 0
if type_fuel == "Diesel":
    price = 2.33
    if club_card == "Yes":
        price -= 0.12


elif type_fuel == "Gas":
    price = 0.93
    if club_card == "Yes":
        price -= 0.08


elif type_fuel == "Gasoline":
    price = 2.22
    if club_card == "Yes":
        price -= 0.18

total = price * quantity_fuel

if 20 <= quantity_fuel <= 25:
    total *= 0.92
elif quantity_fuel > 25:
    total *= 0.90

print(f"{total:.2f} lv.")


