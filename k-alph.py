n = int(input())
l = []
for _ in range(n):
    s = input()
    l.append(s)
k = int(input())

for i in range(len(l)):
    if k <= len(l[i]):
        print(l[i][k-1],end='')
    else:
        continue
