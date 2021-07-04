from numpy import * 
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import *
from matplotlib import cm  
from math import *

""" Здесь прописываются функции, которые необходимы для добавления их в ряд или иных операций """
# Функция для факториала ---------------------------------------------------------------------
def factorial(i):
    m = i
    if m == 0:
        m = 1
    elif m == 1:
        m = 1
    else:
        for k in range(1,i):
            m*= k
    return m

"""------------------------------------------------------------------------------------------ """

#Некоторые данные и массивы для исследования сходимости ряда --------------------------------------
#n = 100
#eps = 10**(-16)
#q = 1/4
#S = zeros(n)
#t = linspace(0,n,n)
#x = 0.1

#Выражение для ряда -------------------------------------------------------------------------------
#i = 1
#S[0] = x**0/factorial(0)
#S[1] = S[0] + x**1/factorial(1)
#while(S[i] - S[i-1] > eps):
#    i+=1
#    S[i] = S[i-1] + x**i/factorial(i)
#    print(S[i],e**x)
    
#S[S==0] = None #Отсечка

#Построение графика сходимости --------------------------------------------------------------------
#figure()
#plot(t,S)
k = 100
n = 100
x = linspace(0,10,k)
y = zeros(k)
j = 1
l = 1
eps = 10**(-10)
S_2 = 0.
#print(x)
for i in range(k):
    S_0 = float(x[i]**0/(factorial(0))**(l))
    S_1 = float(x[i]**1/(factorial(1))**(l))
    print(j,S_1,S_0)
    while(S_1-S_0 > eps):
        j+=1
        S_2 = S_1 + x[i]**j/((factorial(j))**(l))
        S_0 = S_1
        S_1 = S_2
        print(j, S_2, S_1, S_0)

    y[i] = S_2
    j = 1
    

figure()
plot(x,y)     
        

    
    