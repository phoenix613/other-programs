# объявление функции
def is_correct_bracket(text):
    cnt = 0
    for x in text:
        if x == '(':
            cnt += 1
        elif x == ')':
            cnt -= 1
        if cnt < 0:
            return False
    if cnt == 0:
        return True
    else:
        return False
# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))