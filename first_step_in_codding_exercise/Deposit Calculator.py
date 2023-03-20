deposit_sum = int(input())
term_of_deposit_for_month = int(input())
year_percent = float(input())/100

sum = deposit_sum + term_of_deposit_for_month * ((deposit_sum * year_percent)/12)

print(sum)