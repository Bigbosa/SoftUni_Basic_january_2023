meters_climbed = 5_364
day = 1

while True:
    sleeping = input()
    if sleeping == 'END' or day == 5:
        print(f'Failed!')
        print(meters_climbed)
        break
    if sleeping == 'Yes':
        day += 1
    else:
        day = day

    meters_climbed += int(input())

    if meters_climbed >= 8848:
        print(f'Goal reached for {day} days')
        break
