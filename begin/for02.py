a=int(input())
b=int(input())
list=[]
if a>b:
    print("Первое число больше второго")
for i in range(a, b+1):
    list.append(i)
print(list)
print(len(list))