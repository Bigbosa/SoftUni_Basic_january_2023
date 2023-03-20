Num1 = int(input())
Num2 = int(input())
operator = input()

sum = 0

if operator == "+":
    sum = f"{Num1} + {Num2} = {Num1 + Num2}" + (" - even" if (Num1 + Num2) % 2 == 0 else " - odd")
elif operator == "-":
    sum = f"{Num1} - {Num2} = {Num1 - Num2}"+ (" - even" if (Num1 - Num2) % 2 == 0 else " - odd")
elif operator == "*":
    sum = f"{Num1} * {Num2} = {Num1 * Num2}" + (" - even" if (Num1 * Num2) % 2 == 0 else " - odd")
elif Num2 == 0:
   sum = f"Cannot divide {Num1} by zero"
elif operator == "/":
    sum = f"{Num1} / {Num2} = {Num1 / Num2:.2f}"
elif operator == "%":
    sum = f"{Num1} % {Num2} = {Num1 % Num2}"

print(sum)
