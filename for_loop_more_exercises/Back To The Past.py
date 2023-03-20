all_money = float(input())
year_for_live = int(input())

total = all_money
starting_year = 18
sum_ = 12_000


for year in range(1800, year_for_live + 1):
    if year % 2 == 0:
        total = total - sum_
        starting_year += 1

    else:
        total = total - (sum_ + (starting_year * 50))
        starting_year += 1

if total >= 0:
  print(f"Yes! He will live a carefree life and will have {total:.2f} dollars left." )
else:
    print(f"He will need {abs(total):.2f} dollars to survive." )