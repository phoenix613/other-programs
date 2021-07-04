a = [i for i in input().split()]
a.sort()
b =[]
c = a[::-1]

for j in range(len(a)):
    if a != c and a[j-1] != a[j]:
        if a[j-2] == a[j-1]:
            b.append(a[j-1])
    elif a == c and len(a)>1:
        b.append(a[0])
        break        
for j in range(len(b)):
    print(b[j],end =' ')  