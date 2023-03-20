n = int(input())


total_grades = 0
total_grades_sum = 0
while True:
 presentation_name = input()

 if  presentation_name == "Finish":
  break

 grades_sum = 0

 for _ in range(n):
    grades_sum += float(input())

 total_grades_sum += grades_sum
 total_grades += n

 print(f"{presentation_name} - {grades_sum / n:.2f}.")

print(f"Student's final assessment is {total_grades_sum / total_grades:.2f}.")