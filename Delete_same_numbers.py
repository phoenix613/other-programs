n = int(input())

prevnum = ''
b =[] 
for i in range(n):
    a = input()
    if a != prevnum:
        b.append(a)
    else:
        continue
    prevnum = a

for x in b:
    print(x, sep='\n')     