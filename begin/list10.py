n = int(input())
s = []
for i in range(n):
    s.append(input())
p = 0
q = 0
for i in range(len(s)):
    if len(s[i]) > len(s[p]):
        p = i
    if len(s[i]) < len(s[q]):
        q = i
print(s[p])
print(s[q])
print(len(s[p]))
print(len(s[q]))
