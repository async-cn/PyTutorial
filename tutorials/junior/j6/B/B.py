m = int(input())

if m <= 180:
    print(m*5)
elif m <= 400:
    print(900 + (m-180)*7)
else:
    print(2440 + (m-400)*9)