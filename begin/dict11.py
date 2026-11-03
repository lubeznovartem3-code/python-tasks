n = int(input())
d = {}
for i in range(n):
    w = input()
    d[w] = d.get(w, 0) + 1
for k, v in d.items():
    print(f"{k}: {v}")
