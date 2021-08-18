#Функции кодирования/декодирования сообщения-----------------------------------
def coder (lang, s, n):
    b = ''
    if lang == 'английский':
        for x in s:
            if x.isalpha() == True:
                a = ord(x.lower())
                a = (a + n - 96) % 26 + 96
                if x.lower() != x:
                    b += chr(a).upper()
                else:
                    b += chr(a)
            else:
                b += x
        return b        
    
        
    elif lang == 'русский':
        for x in s:
            if x.isalpha() == True:
                a = ord(x.lower())
                a = (a + n - 1071) % 32 + 1071
                if x.lower() != x:
                    b += chr(a).upper()
                else:
                    b += chr(a)
            else:
                b += x
        return b

def decoder (lang, s, n):
    b = ''
    if lang == 'английский':
        for x in s:
            if x.isalpha() == True:
                a = ord(x.lower())
                a = (a - n - 96) % 26 + 96
                if x.lower() != x:
                    b += chr(a).upper()
                    print(x)
                else:
                    b += chr(a)
            else:
                b += x
        return b        
    
        
    elif lang == 'русский':
        for x in s:
            if x.isalpha() == True:
                a = ord(x.lower())
                a = (a - n - 1071) % 32 + 1071
                if x.lower() != x:
                    b += chr(a).upper()
                else:
                    b += chr(a)
            else:
                b += x
        return b 
#Защита -----------------------------------------------------------------------    
def is_valid_num(n):
    return n.isdigit()
def is_valid_lang(lang):
    return lang in ['русский','английский']
def is_valid_var(R):
    return R in ['+','-']
def right_lang(lang,s):
    pass
def is_valid_again (b):
    return b in ['да','нет']
#------------------------------------------------------------------------------
def again (a):
    b = input('Желаете попробовать ещё раз? (да/нет)')
    if is_valid_again(b) == True:
        if b == 'нет':
            return False
        elif b == 'да':
            return True

def defin_code ():
    a = True
    while a == True:
        n = input('Введите величину сдвига: ')
        if is_valid_num(n) == True:
            lang = input('Введите язык (русский, английский): ')
            if is_valid_lang(lang) == True:
                R = input('Кодировать (+) или декодировать (-)? ')
                if is_valid_var(R) == True:
                    if R == '+':
                        s = input('Введите текст для проведения кодирования: ')
                        s = coder(lang, s, int(n))
                        print(s)
                        a = again(a)                  
                    else:
                        s = input('Введите текст для проведения декодирования: ')
                        s = decoder(lang,s,int(n))
                        print(s)
                        a = again(a)
                else:
                    print('Не понимаю, что нужно сделать. Попробуйте ещё раз.')
            else:
                print('Введён неверный язык, попробуйте ешё раз')
                continue
        else:
            print('Введено не число!')
            continue
#------------------------------------------------------------------------------    
n = 25
for i in range(n):
    s = 'Hawnj pk swhg xabkna ukq nqj.'
    s = decoder('английский', s, i)
    print(s)




       