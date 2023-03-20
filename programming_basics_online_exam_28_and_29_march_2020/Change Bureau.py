first_sum = int(input())
second_sum = float(input())
sum_ = float(input())

bitcoin = first_sum * 1168
uan = second_sum * 0.15
dollar = uan * 1.76
fee = sum_ / 100

total_sum = (bitcoin + dollar) / 1.95
commissions = total_sum * fee
all_sum = total_sum - commissions

print(f"{all_sum:.2f}")