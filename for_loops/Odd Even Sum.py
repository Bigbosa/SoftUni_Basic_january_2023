number = int(input())

even = 0
odd = 0
for num in range(1,number +1):
    current_sum = int(input())
    if num % 2 ==0:
     even += current_sum
    else:
       odd += current_sum
if even == odd:
    print(f"Yes\nSum = {even} ")
elif even != odd:
    diff = abs(odd - even)
    print(f"No\nDiff = {diff}")