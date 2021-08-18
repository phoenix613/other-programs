from random import *

#Блок функций------------------------------------------------------------------
def rand_num (k):
    return randint(1,k)

def is_valid (s,k):
    return s.isdigit() and 1 <= int(s) <= k

def game ():
    k = int(input('Введите правую границу диапазона угадывания: '))
    n = rand_num(k)
    cnt = 1
    s = input(f'Введите любое число от 1 до {k}: ')
    while n != int(s):
        if is_valid(s,k) == True:
            s = int(s)
            if s < n:
                s = input('Ваше число меньше загаданного, попробуйте ещё разок: ')
                cnt += 1
                continue
            elif s > n:
                s = input('Ваше число больше загаданного, попробуйте ещё разок: ')
                cnt += 1
                continue
        else:
            s = input(f'А может быть всё-таки введём целое число от 1 до {k}? ')
            continue
    return cnt            
    
#Проведение игры---------------------------------------------------------------
print('Добро пожаловать в числовую угадайку')

a = True
while a == True:
    cnt = game()
    print('Вы угадали, поздравляем!')
    print(f'Число угадано с {cnt} попытки')
    b = input('Хотите ли Вы продолжить? (Да/Нет) ')
    if b == 'Нет':
        a = False
    elif b == 'Да':
        continue
    else:
        b = input('Я Вас не понимаю, введите ещё раз: ')

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')        
#------------------------------------------------------------------------------
