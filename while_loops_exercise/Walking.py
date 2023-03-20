Goal = 10_000
step_walked = 0

while step_walked < Goal:
    steps = input()

    if steps == "Going home":
        step_walked += int(input())
        break

    step_walked += int(steps)

if step_walked >= Goal:
     print("Goal reached! Good job!")
     print(f"{step_walked - Goal} steps over the goal!")
else:
    print(f"{Goal - step_walked} more steps to reach goal.")  
