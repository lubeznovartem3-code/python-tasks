n = int(input())
s = []
for i in range(n):
    s.append(input())
c = input()
print([x for x in s if x[:1] == c])
