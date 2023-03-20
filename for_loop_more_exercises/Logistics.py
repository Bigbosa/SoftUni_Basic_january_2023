number = int(input())


microbus = 0
truck = 0
train = 0
total_sum = 0
tons = 0
price = 0
microbus_tons = 0
truck_tons = 0
train_tons = 0

for _ in range(1, number + 1):
    load = int(input())
    tons += load

    if load <= 3:
       microbus += + load * 200
       microbus_tons += load

    elif 4 <= load <= 11:
        truck += + load * 175
        truck_tons += load

    elif load > 11:
        train += + load * 120
        train_tons += load

total_sum = microbus + truck + train
price = total_sum / tons

percent_microbus = (microbus_tons / tons) * 100
percent_truck = (truck_tons / tons) * 100
percent_train = (train_tons / tons) * 100

print(f"{price:.2f}")
print(f"{percent_microbus:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")

