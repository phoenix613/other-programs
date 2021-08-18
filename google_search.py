n = int(input())
l = []
for _ in range(n):
    s = input()
    l.append(s)
    
k = int(input())
le = []
for _ in range(k):
    s = input()
    le.append(s)
cnt = 0
for i in range(n):
    for j in range(k):
        if le[j].lower() in l[i].lower():
            cnt+=1
    if cnt == k:
        print(l[i])
    cnt = 0  