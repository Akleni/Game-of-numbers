f = open('number.txt','r', encoding='utf-8')
a = f.read()
num = 0
print('Угадай число')
print('Вам нужно угадать число от 1 до 100 за 6 попыток. Удачи!')

for i in range(1,7):
    num += 1
    b = int(input('Ваше число: '))
    if int(a) == b:
        print(f'Вы угадали число за {num} попыток!')
        break
    elif int(a) < b:
        print('Вы не угадали! Секретное число меньше того что вы ввели')
    elif int(a) > b:
        print('Вы не угадали! Секретное число больше того что вы ввели')

print(f'Число было {a}')