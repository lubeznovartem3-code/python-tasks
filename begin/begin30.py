pi = 3.14
a = float(input())
if a<0 or a>2*pi:
    print("не шути тут")
else:
    grad = a*(180/pi)
    print(f"{grad:.2f} градусов")