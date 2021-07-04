b = []
a=[0]
while a[0] != 'end':
    a = [i for i in input().split()]
    b.append(a)       
b.remove(['end'])
c =[[0 for j in range(len(b[i]))] for i in range(len(b))]
for i in range(len(c)):
    if len(c) > 1 or len(c[i]) > 1:
        for j in range(len(c[i])):
            if (j + 1) <= len(c[i])-1 and (i + 1) <= len(c)-1:
                c[i][j] =(int(b[i-1][j]) + int(b[i+1][j]) + int(b[i][j-1]) + int(b[i][j+1]))
            else:
                c[i][j] = (int(b[i-1][j]) + int(b[i][j-1]) + int(b[i+1 - len(c)][j]) + int(b[i][j+1 - len(c[i])])) 
    else:
        c[0][0] = int(b[0][0])
        c[0][0]*=4
        #print(c)
for i in range(len(c)):
    print(end ='\n')
    for j in range(len(c[i])):
        print(c[i][j], end = ' ') 