
number_of_days = int(input())

counter = 0
total = 0
middle_degrees = 0
for number_of_days in range(0,number_of_days):
    liter = float(input())
    degrees = float(input())

    total += liter
    middle_degrees = liter * degrees
    counter += middle_degrees

total_sum = counter / total

print(f"Liter: {total:.2f}")

print(f"Degrees: {total_sum:.2f}")

if total_sum < 38:
    print("Not good, you should baking!" )
elif 38 <= total_sum <=42:
    print("Super!" )
elif total_sum > 42:
    print("Dilution with distilled water!" )

