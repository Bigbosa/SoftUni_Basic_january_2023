from math import floor
number_of_tournaments = int(input())
number_of_point = int(input())

won_tournaments = 0
sum_points = 0

for _ in range(number_of_tournaments):
    moment_in_tournament = (input())

    if moment_in_tournament == "W":
        won_tournaments +=1
        sum_points +=  2000
    elif moment_in_tournament == "F":
         sum_points +=1200
    elif moment_in_tournament == "SF":
         sum_points += 720




print(f"Final points: {sum_points + number_of_point}")
print(f"Average points: {floor(sum_points / number_of_tournaments)}")
print(f"{won_tournaments/number_of_tournaments *100:.2f}%")





