a=input()
b=int(input())
a=list(a)
try:
    print(a[b])
except IndexError:
    print("нет такого символа")