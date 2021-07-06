n = int(input())

mx = 0
mn = 10

while n != 0:
    ld = n % 10
    if ld > mx:
        mx = ld
    if ld < mn:
        mn = ld
    n = n // 10

print('Максимальная цифра равна', mx)
print('Минимальная цифра равна', mn)