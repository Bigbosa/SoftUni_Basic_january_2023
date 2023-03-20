period = int(input())

total_treated_patients = 0
total_untreated_patients = 0
doctors = 7
new_doctor = 0

for days in range(1, period + 1):
    number = int(input())
    if days % 3 == 0 and total_untreated_patients > total_treated_patients:
        new_doctor += 1

    if number <= (doctors + new_doctor):
        total_treated_patients += + number

    else:
        total_treated_patients += + (doctors + new_doctor)
        total_untreated_patients += + number - (doctors + new_doctor)

print(f"Treated patients: {total_treated_patients}.")
print(f"Untreated patients: {total_untreated_patients}.")