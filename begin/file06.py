k = int(input())
name = input()
with open(name, encoding="utf-8") as f:
    a = [int(line) for line in f if line.strip()]
if 1 <= k <= len(a):
    print(a[k - 1])
else:
    print(-1)
