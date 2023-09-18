a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a == b and a != c:
    print('2')
elif b == c and b != a:
    print('2')
elif c == a and c != b:
    print('2')
elif a != b and b != c and a != c:
    print('0')
elif a == b and a == c and b == c:
    print('3')