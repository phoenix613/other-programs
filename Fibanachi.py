n = int(input())


#Первый способ, классический, через вспомогательную переменную ------------

sum1 = 0
sum2 = 1

k = 0
for _ in range(n):
    k = sum2 + sum1
    print(sum2, end=' ')
    sum1 = sum2
    sum2 = k
  
print(end='\n') #Разделение
#Второй способ, более экономный на код ------------------------------------

sum1 = 0
sum2 = 1
    
for _ in range(n):
    sum1, sum2 = sum2, sum1 + sum2
    print(sum1, end=' ')    
    