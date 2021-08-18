from random import *
import matplotlib.pyplot as plt

#Генерация броска монетки -----------------------------------------------------
def OP(n,k):
    c  = ''
    for _ in range(n):
        n = randint(0,k)
        if n % 2 == 0:
           c += 'О'
        else:
           c += 'Р'
    return c
#Подсчёт вхождений, включая пересекающиеся-------------------------------------
def count_o(c,x):
    cnt = 0
    for i in range(len(c)):
        if x in c[i:i+2]:
            cnt += 1
    return cnt        
#Функция для задания числа измерений, бросков и тд...--------------------------
def measure(x,n,k,l):
    cnt = 0
    for _ in range(l):
        c = OP(n,k)
        if x in c:
            cnt += 1
    return l, cnt/l
#Среднее значение--------------------------------------------------------------
def avrg (P):
    return sum(P)/len(P)
#------------------------------------------------------------------------------        
n = int(input('Число бросков: '))
k = int(input('Коэфф. рандомайзера: '))
x = input('Вероятность какой последовательности нужно найти: ')
Cnt = []
P = []
m = 500
l = 2
for _ in range(m):
    cnt, p = measure(x,n,k,l)
    Cnt.append(cnt)
    P.append(p)
    l+=10 
a = [round(avrg(P),3) for i in range(len(P))]
#График частотности события----------------------------------------------------    
plt.figure()
plt.plot(Cnt,P)
plt.plot(Cnt,a,'red')
plt.title(f'P =  {round(avrg(P),3)}')       
        