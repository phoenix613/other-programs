num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
        flag = False

if num != 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')