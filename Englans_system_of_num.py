n = input()

b = ''
n = n[::-1]
i = 3
while abs(i) < len(n):
    b += n[i-3:i] + ','
    i+=3
b += n[i-3:]    
print(b[::-1])    
        
   