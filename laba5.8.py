import numpy as np
import matplotlib.pyplot as plt

# Задаем количество точек для построения графика
N = 256
V = np.linspace(0, 2*np.pi, N)  # Массив истинных аномалий θ

# Параметры для "эллипсоидных" ИСЗ
p_values = [6, 6, 6, 6, 6]      # Параметр орбиты (одинаковый для всех)
e_values = [0.18, 0.33, 0.55, 0.67, 0.89]  # Эксцентриситеты
labels = [
    'Эллипсоидная 1',
    'Эллипсоидная 2',
    'Эллипсоидная 3',
    'Эллипсоидная 4',
    'Эллипсоидная 5'
]

# Создаем фигуру
plt.figure(figsize=(10, 8))

# Цикл по всем орбитам
for i, (p, e, label) in enumerate(zip(p_values, e_values, labels)):
    # Рассчитываем радиус r по формуле: r = p / (1 + e * cos(θ))
    r = p / (1 + e * np.cos(V))
    
    # Построение орбиты в полярной системе координат
    plt.polar(V, r, label=label)

# Настройки графика
plt.grid(True)
plt.title('Эллиптические орбиты ИСЗ')
plt.legend(loc='upper right')

plt.show()