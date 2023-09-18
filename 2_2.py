def print_pyramid(n):
    # Определение ширины пирамиды
    width = 2 * n - 1

    for i in range(1, n + 1):
        # Выводим пробелы перед числами
        for j in range(width - i, 0, -1):
            print(' ', end='')

        # Выводим числа от 1 до i
        for j in range(1, i + 1):
            print(j, end='')

        # Выводим числа от i-1 до 1 в обратном порядке
        for j in range(i - 1, 0, -1):
            print(j, end='')

        print()  # Переход на новую строку


# Запрашиваем у пользователя количество ступенек
n = int(input("Введите количество ступенек: "))

# Выводим пирамиду
print_pyramid(n)