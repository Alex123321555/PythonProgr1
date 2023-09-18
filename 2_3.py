def print_pyramid(n):
    # Определение максимального разряда числа
    max_digits = len(str(n))

    for i in range(1, n + 1):
        # Выводим пробелы перед числами
        for _ in range(n - i):
            print(' '.rjust(max_digits), end=' ')

        # Выводим числа от 1 до i
        for j in range(1, i + 1):
            print(str(j).rjust(max_digits), end=' ')

        # Выводим числа от i-1 до 1 в обратном порядке
        for j in range(i - 1, 0, -1):
            print(str(j).rjust(max_digits), end=' ')

        # Переход на новую строку
        print()

# Запрашиваем у пользователя количество уровней пирамиды
n = int(input("Введите количество уровней пирамиды: "))

# Выводим пирамиду
print_pyramid(n)

input("Нажмите Enter для завершения программы")