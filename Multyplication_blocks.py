a = int(input())
b = int(input())
c = int(input())
d = int(input())

if(a <= b and c <= d):
    print(end='\t')
    for j in range(c,d+1):
        print(j,end='\t')
    for i in range(a,b+1):
        print('\n',i,end='\t')
        for j in range(c,d+1):
            print(i*j,end='\t')
else:
    print('Неверный ввод данных')