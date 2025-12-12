a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

# Список хранение чисел интервала
result = []

# Проверка чисел
if 1 <= a <= 3:
 result.append(a)

if 1 <= b <= 3:
 result.append(b)

if 1 <= c <= 3:
 result.append(c)

# Результат
if len(result) == 0:
 print("Нет чисел, принадлежащих интервалу [1,3]")
else:
 print("Числа, принадлежащие интервалу [1,3]:", result)
