number_of_floor = int(input())
number_of_room = int(input())


for current_floor in range(number_of_floor, 0, -1):
    for number in range(number_of_room):
        if current_floor == number_of_floor:
            print(f"L{current_floor}{number}", end=" ")
        else:
         if current_floor % 2 != 0:
            print(f"A{current_floor}{number}", end=" ")
         else:
            print(f"O{current_floor}{number}", end=" ")


    print("")