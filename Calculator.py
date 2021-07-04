a = float(input())
b = float(input())
c = input()

if c == '+':
  print(a + b)
elif c == '-':
  print(a - b)
elif c == '*':
  print(a * b)
elif c == '/':
    if b!=0:
      print(a/b)
    else:
      print('Деление на 0!')
elif c == 'mod':
    if b!=0:
      print(a % b)
    else:
      print('Деление на 0!')
elif c == 'div':
    if b!=0:
       print(a // b)
    else:
       print('Деление на 0!')
elif c == 'pow':
  print(a**b)
else:
  print('Ошибка ввода!')