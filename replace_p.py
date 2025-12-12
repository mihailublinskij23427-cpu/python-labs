# Запрос строки
text = input("Введите строоку: ")

# Длина строки
n = len(text)

# Граница первой половины
half = n // 2

# Преобразуем первую половину строки
new_text = ""
for i in range(n):
 if i < half and text[i] == 'п':
  new_text += '*'
 else:
  new_text += text[i]

# Выводим результат
print("Результат:", new_text)
