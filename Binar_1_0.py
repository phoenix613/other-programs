n = int(input())

cnt = 0
cntmax = 0

for i in range(n):
    a = int(input())
    
    if a == 1:
        cnt+=1
    elif a == 0 and cnt > cntmax:
        cntmax = cnt
        cnt = 0
    else:
        cnt = 0
        
print(max(cntmax,cnt))              