import os

a = input()
b = input()
if os.path.exists(a):
    src = a
    dst = b
else:
    src = b
    dst = a
with open(src, encoding="utf-8") as f:
    x = [int(line) for line in f if line.strip()]
with open(dst, "w", encoding="utf-8") as f:
    f.write(str(x[-1]) + "\n")
    f.write(str(x[0]) + "\n")
