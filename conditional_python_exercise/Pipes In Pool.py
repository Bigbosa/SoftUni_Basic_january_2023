v = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

debit_1 = P1 * H
debit_2 = P2 * H

sum_1 =  debit_1 + debit_2



if sum_1<=v:
    p1_field = debit_1 / sum_1 * 100
    p2_field = debit_2 / sum_1 * 100
    pool_field = sum_1 / v * 100
    print(f"The pool is {pool_field:.2f}% full. Pipe 1: {p1_field:.2f}%. Pipe 2: {p2_field:.2f}%.")

else:
    print(f"For {H} hours the pool overflows with {sum_1 - v} liters.")