n = int(input())

mx1 = -1
mx2 = -1

for _ in range(n):
    a = int(input())
    if mx2 < a < mx1:
        mx2 = a
    elif mx2 < a and mx1 < a:
        mx2 = mx1
        mx1 = a
        

print(mx1)
print(mx2)        