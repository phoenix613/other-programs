s = int(input())
st =''

while(s > 0):
    st += str(s%2)
    s //= 2

for i in range(len(st)-1,-1,-1):
    print(st[i],end='')    
    