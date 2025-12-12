import math

# Значения
x=float(input("Введите значение x: "))
t=float(input("Введите значение t: "))

if t < 0:
 print("Ошибка: число под корнем не может быть отрицательным.")

else:
# Вычисляем знаменатель
 denominator = math.sqrt(t) - abs(math.sin(t))
 if denominator == 0:
  print("Ошибка; знаменатель равен нулю - деление невозможно.")
 else:
# Вычисляем числитель
      numerator = 9 * math.pi*t+10*math.cos(x)

# Вычисляем Z
      z = (numerator / denominator) * math.exp(x)

# Выводим результат
print(f"Результат; {z:.2f}")
