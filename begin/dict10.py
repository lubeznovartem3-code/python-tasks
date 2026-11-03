n = int(input())
d = {}
for i in range(n):
    k = input()
    v = int(input())
    d[k] = v
for k, v in d.items():
    print(f"{k}: {v}")
