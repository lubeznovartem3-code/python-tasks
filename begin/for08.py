a=int(input())
b=int(input())
summ = 1
if a>b:
    print("Первое число больше второго")
for i in range(a, b+1):
    summ = summ*i
print(summ)