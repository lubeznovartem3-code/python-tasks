a = int(input())
b = int(input())
mini = b
s = 0
c = 0
while c < a:
    if a - c < mini:
        print(s)
        break
    else:    
        c = c + b
        s = s + 1
        
