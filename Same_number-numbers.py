n = int(input())

flag = True
temp = n % 10

while n != 0:
    ld = n % 10
    if temp != ld:     #Можно менять знак, чтобы решать четыре разные задачи
        flag = False
    temp = ld    
    n //= 10
    
if flag == True:
    print('YES')
else:
    print('NO')    