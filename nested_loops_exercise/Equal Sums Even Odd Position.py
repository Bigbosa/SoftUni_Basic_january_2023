number_1 = int(input())
number_2 = int(input())

for i in range(number_1,number_2 + 1):
    eve_sum , odd_sum = 0,0

    for j , h in enumerate(str(i)):
        if j % 2 == 0:
            eve_sum += int(h)
        else:
            odd_sum += int(h)
    if odd_sum == eve_sum:
        print(i, end=" ")