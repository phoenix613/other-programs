n = int(input())

a = n//100000

b = (n%100000)//10000

c = (n%10000)//1000

d = (n%1000)//100

e = (n%100)//10

f = (n%10)

if a + b + c == d + e + f:
    print('Счастливый')
else:
    print('Обычный')