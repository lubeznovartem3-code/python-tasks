a=int(input())
b=int(input())
summ = 0
if a>b:
    print("Первое число больше второго")
for i in range(a, b+1):
    summ = summ + i**2
print(summ)