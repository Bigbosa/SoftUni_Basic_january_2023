import math
meters = int(input())
one_grapes = float(input())
liters_for_vine = int(input())
number_of_workers = int(input())

kg_graves = 2.5
meter_vine = 0.40

total_grapes = meters * one_grapes
vine = (meter_vine * total_grapes)/ kg_graves


if vine >= liters_for_vine:
    total_vine = vine - liters_for_vine
    vine_for_workers = total_vine / number_of_workers
    print(f"Good harvest this year! Total wine: {math.floor(vine)} liters.")
    print(f"{math.ceil(total_vine)} liters left -> {math.ceil(vine_for_workers)} liters per person.")
else:
    total_vine_2 = abs(liters_for_vine - vine)
    print(f"It will be a tough winter! More {math.floor(total_vine_2)} liters wine needed.")
  