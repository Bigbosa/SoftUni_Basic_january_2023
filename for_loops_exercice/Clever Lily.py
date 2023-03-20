age_lili = int(input())
washing_machine = float(input())
price_for_one_toy = int(input())

money_given = 10
money_from_gift = 0
taken_from_brother = 1
for age in range(1, age_lili + 1):

    if age % 2 == 0:
        money_from_gift += money_given - taken_from_brother
        money_given += 10
    else:
        money_from_gift += price_for_one_toy

if money_from_gift >= washing_machine:
   print(f"Yes! {money_from_gift - washing_machine:.2f}")
else:
    print(f"No! {washing_machine - money_from_gift:.2f}")
