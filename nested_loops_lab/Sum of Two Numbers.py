first_number = int(input())
second_number = int(input())
magic_number = int(input())

combination = 0

stop = 0

for i in range(first_number,second_number +1 ):
   for j in range(first_number, second_number + 1):
       if i + j == magic_number:
           combination += 1
           total = i + j
           stop += 1
           print(f"Combination N:{combination} ({i} + {j} = "f"{magic_number})")
           break
       else:
           combination += 1

   if i + j == magic_number:
           total = i + j
           stop += 1
           break

if stop != 2:
    print(f"{combination} combinations - neither equals {magic_number}")




