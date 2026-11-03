n = int(input())
d = {}
for i in range(n):
    k = input()
    v = int(input())
    d[k] = v
q = input()
if q in d:
    print(d[q])
else:
    print("нет такого ключа")
