# Запрашиваем у пользователя количество ступенек
n = int(input("Введите количество ступенек: "))

# Генерируем и выводим лестницу
for i in range(1, n + 1):
    stair = ''.join(str(j) for j in range(1, i + 1))
    print(stair)