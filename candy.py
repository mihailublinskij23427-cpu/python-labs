# Цена за 1 кг
price_per_kg = float(input("Введите цену 1 кг конфет; "))

print("\nСтоимость конфет;")
print("-" * 20)

# Цикл
for weight in range(1, 11):
 cost = price_per_kg * weight
 print(f"{weight} кг: {cost:.2f} руб.")
