n = int(input())
c = [[0 for j in range(n)] for i in range(n)]
m = n - 1 
k = n - 1
cnt = 1
m=0
c[n//2][n//2]=n*n
for v in range(n//2):
    #Заполнение верхней горизонтальной матрицы
    for i in range(n-m):
        c[v][i+v] = cnt
        cnt+=1
        
    #Заполнение правой вертикальной матрицы    
    for i in range(v+1, n-v):
        c[i][-v-1] = cnt
        cnt+=1
        
    #Заполнение нижней горизонтальной матрицы
    for i in range(v+1, n-v):
        c[-v-1][-i-1] = cnt
        cnt+=1
        
    #Заполнение левой вертикальной матрицы
    for i in range(v+1, n-(v+1)):
        c[-i-1][v] = cnt
        cnt+=1
    
    m+=2    
for i in range(len(c)):
    print(end ='\n')
    for j in range(len(c[i])):
        print(c[i][j], end = ' ') 