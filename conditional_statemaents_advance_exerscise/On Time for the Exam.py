
exam_hours = int(input())
exam_minutes = int(input())
student_hours = int(input())
minutes_on_time = int(input())

exam_minute = exam_hours * 60 + exam_minutes
student_time = student_hours * 60 + minutes_on_time

time_diff = exam_minute - student_time


if time_diff > 30:
    print("Early")
elif time_diff < 0:
    print("Late")
else:
    print("On time")

hours = 0
minutes = abs(time_diff)

result = ""

if minutes >= 60:
    hours = minutes // 60
    minutes = minutes % 60

if hours > 0:
    result += f"{hours}:{minutes:02d} hours"
elif minutes > 0:
    result += f"{minutes} minutes"

if time_diff > 0:
    result += " before the start"
elif time_diff < 0:
    result += " after the start"

print(result)