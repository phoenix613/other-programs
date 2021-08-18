a = int(input())
b = int(input())

summ1 = 0
summ2 = 0
value = 0

for i in range(a,b+1):
    for j in range(1,i+1):
        if i % j == 0:
            summ1 += j
        
    if summ1 >= summ2:
        summ2 = summ1
        value = i
    summ1 = 0  
    
print(value, summ2)        