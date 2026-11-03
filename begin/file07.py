name = input()
with open(name, encoding="utf-8") as f:
    a = [int(line) for line in f if line.strip()]
print(a[0])
print(a[1])
print(a[-2])
print(a[-1])
