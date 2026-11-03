n = int(input())
a = n

if n%2 == 0:
    while a >= 2:
        a = a-2
        if a == 0:
            break
        n = n * (a)
    print(n)
else:
    while a >= 1:
        a = a-2
        if a <= 0:
            break
        n = n * (a)
    print(n)