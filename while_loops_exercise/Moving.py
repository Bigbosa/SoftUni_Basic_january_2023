total_spaces = int(input())  * int(input()) * int(input())
free_spaces = 0

while total_spaces > free_spaces:
    box = input()

    if box == "Done":
        print(f"{total_spaces - free_spaces} Cubic meters left.")
        break

    free_spaces += int(box)
else:
    print(f"No more free space! You need {free_spaces - total_spaces} Cubic meters more.")