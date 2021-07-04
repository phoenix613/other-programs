n = int(input())

if  10 <= n % 100 <= 20:
  print(n, 'программистов')
  
elif n%10 != 0 and n%10 == 1 :
  print(n,' программист')
  
elif n%10 != 0 and 2 <= n%10 <= 4:
  print(n, 'программиста')
  
elif n%10 != 0 and 5 <= n%10 <= 9:
  print(n, 'программистов') 
  
elif n%10 == 0:
  print(n, 'программистов')