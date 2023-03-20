buget = float(input())

number_gpu = int(input())
number_cpu = int(input())
number_ram = int(input())

gpu = number_gpu * 250
cpu = number_cpu * gpu * 0.35
ram = number_ram * gpu * 0.10

total_sum = gpu + cpu + ram

if number_gpu > number_cpu:
    total_sum *= (1 - 0.15)

if total_sum <= buget:
    print(f"You have {buget - total_sum:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_sum - buget:.2f} leva more!")



