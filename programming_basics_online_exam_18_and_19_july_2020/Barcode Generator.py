number = input()
end = input()

for num1 in range(int(number[0]), int(end[0]) + 1):
    for num2 in range(int(number[1]), int(end[1]) + 1):
        for num3 in range(int(number[2]), int(end[2]) + 1):
          for num4 in range(int(number[3]), int(end[3]) + 1):
              if num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0 and num4 % 2 != 0:
                  print(f"{num1}{num2}{num3}{num4}", end= " ")





