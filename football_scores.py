n, m = map(int,input().split())

cnt = 0

d = {}
ids = []
for i in range(n):
    d[i] = 0
   

for i in range(m):
    a, b = map(int,input().split())
    ids = [int(p) for p in input().split()]
    for j in range(5):
        d[ids[j]] += a - b
    for j in range(5,10):
        d[ids[j]] += b - a
        
    for i in range(n):
        if d[0] < d[i]:
            cnt += 1
    
    print(cnt)        
    
           