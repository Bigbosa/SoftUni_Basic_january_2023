number_of_students = int(input())

fail_students = 0
between_three_and_four = 0
between_four_and_five = 0
top_students = 0
average_grade = 0


for _ in range(1, number_of_students +1):
    grades = float(input())
    average_grade += grades

    if grades >= 5:
       top_students += 1

    elif 3.99 < grades <= 4.99:
       between_four_and_five += 1

    elif 2.99 < grades <= 3.99:
       between_three_and_four += 1

    elif grades <= 2.99:
        fail_students += 1

average_grade = average_grade / number_of_students
top_students_percent = (top_students / number_of_students)*100
between_four_and_five_percent = (between_four_and_five / number_of_students) * 100
between_three_and_four_percent = (between_three_and_four / number_of_students) * 100
fail_students_percent = (fail_students / number_of_students) * 100


print(f"Top students: {top_students_percent:.2f}%")
print(f"Between 4.00 and 4.99: {between_four_and_five_percent:.2f}%")
print(f"Between 3.00 and 3.99: {between_three_and_four_percent:.2f}%")
print(f"Fail: {fail_students_percent:.2f}%")
print(f"Average: {average_grade:.2f}")