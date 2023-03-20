n = int(input())
m = int(input())
s = int(input())


addresses = []


for i in range(m, n-1, -1):
    if i % 2 == 0 and i % 3 == 0:
        if i != s:
            addresses.append(i)
        else:
            break


print(' '.join(map(str, addresses)))