bad_grades = int(input())
failed_times = 0
failed_problems_count = 0
grades_sum = 0
last_problems = ''
has_failed = True

while failed_times < bad_grades:
    problems_name = input()
    if problems_name == 'Enough':
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
         failed_times += 1
    grades_sum += grade
    failed_problems_count += 1
    last_problems = problems_name
if has_failed:
    print(f"You need a break, {bad_grades} poor grades.")
else:
    print(f"Average score: {grades_sum / failed_problems_count:.2f}")
    print(f"Number of problems: {failed_problems_count}")
    print(f"Last problem: {last_problems}")