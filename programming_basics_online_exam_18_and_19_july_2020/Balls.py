n = int(input())

red = 0
orange = 0
yellow = 0
white = 0
black = 0
dots = 0
other = 0

for token in range(n):
 color = input()

 if color == "red":
     red += 1
     dots += 5

 elif color == "orange":
     orange += 1
     dots += 10

 elif color == "yellow":
       yellow += 1
       dots += 15

 elif color == "white":
     white += 1
     dots += 20

 elif color == "black":
     black += 1
     dots = int(dots / 2)
 else:
     other += 1

print(f"Total points: {dots}")
print(f"Red balls: {red}")
print(f"Orange balls: {orange}")
print(f"Yellow balls: {yellow}")
print(f"White balls: {white}")
print(f"Other colors picked: {other}")
print(f"Divides from black balls: {black}")


