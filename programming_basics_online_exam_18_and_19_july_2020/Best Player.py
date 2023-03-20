max_goals = 0
max_goals_player = ""


player = input()
while player != "END":
    goals = int(input())
    if goals > max_goals:
        max_goals = goals
        max_goals_player = player
    if goals >= 10:
        break
    player = input()

print(f"{max_goals_player} is the best player!")
if max_goals >= 3:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")