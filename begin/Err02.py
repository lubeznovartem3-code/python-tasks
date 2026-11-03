a=int(input())
b=int(input())
c=0
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Нельзя делить на ноль")
