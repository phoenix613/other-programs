# объявление функции
def is_valid_password(p):
    cnt = 0
    m = p.split(':')
    a = m[0]
    b = m[1]
    c = m[2]
    if len(m) > 3:
        return False
   #--------------------------------- 
    if a == a[::-1]:
        cnt += 1
   #---------------------------------     
    flag = True
    if int(b) == 1:
        flag = False
    else:    
        for i in range(2,int(b)//2+1):
            if int(b) % i  == 0:
                flag = False
                break
    if flag == True:
        cnt += 1
   #---------------------------------     
    if int(c) % 2 == 0:
        cnt+=1
   #---------------------------------     
    if cnt == 3:
        return True
    else:
        return False

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))