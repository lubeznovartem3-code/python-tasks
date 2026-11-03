a=input()
b=input()
a=list(a)
try:
    b=int(b)
    print(a[b])

except ValueError:
    print("Число введите")
except IndexError:
    print("Нет такого символа")