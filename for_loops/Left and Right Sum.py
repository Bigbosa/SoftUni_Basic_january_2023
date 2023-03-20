number = int(input())

left_sum = 0
right_sum = 0
diff = 0
for num in range(number):
   current_sum = int(input())
   left_sum += current_sum
for num in range(number):
    current_sum = int(input())
    right_sum += current_sum

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
elif left_sum != right_sum:
    diff = abs(right_sum - left_sum)
    print(f"No, diff = {diff}")

