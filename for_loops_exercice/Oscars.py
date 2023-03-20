MAX_POINTS = 1250.5

name_of_actor = input()
points_1 = float(input())
judge = int(input())

for _ in range(judge):
   name_of_judge = input()
   points = float(input())

   points_1 += len(name_of_judge) * points / 2

   if points_1 > MAX_POINTS:
       print(f"Congratulations, {name_of_actor} got a nominee for leading role with {points_1:.1f}!")
       break
else:
    print(f"Sorry, {name_of_actor} you need {MAX_POINTS - points_1:.1f} more!")