import os

c = 0
for i in range(4):
    name = input()
    if os.path.exists(name):
        c += 1
print(c)
