n = int(input())
a = 3
while True:
    if a == n:
        print("True")
        break
    elif a > n:
        print("False")
        break
    else:
        a = a*3