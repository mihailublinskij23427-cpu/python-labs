import numpy as np
import matplotlib.pyplot as plt

# Принимаем радиус Земли в километрах
R_earth = 6371.0  # км

# Функция для расчёта ЛИНЕЙНОГО радиуса ЗР (в км) по высоте h
def calculate_zr_radius(h):
    # Центральный угол θ (в радианах)
    theta_rad = np.arccos(R_earth / (R_earth + h))
    # Линейный радиус ЗР = R_earth * θ
    zr_radius_km = R_earth * theta_rad
    return zr_radius_km

# Определяем список всех орбит из таблицы

# Эллипсоидные орбиты
elliptical_orbits = [
    (6, 0.18, 'Эллипсоидная 1'),
    (6, 0.33, 'Эллипсоидная 2'),
    (6, 0.55, 'Эллипсоидная 3'),
    (6, 0.67, 'Эллипсоидная 4'),
    (6, 0.89, 'Эллипсоидная 5')
]

# Остальные орбиты
other_orbits = [
    (3, 0, 'Круговая'),
    (2, 1, 'Параболическая'),      # e=1
    (2, 1.7, 'Гиперболическая 1'),
    (1, 2.3, 'Гиперболическая 2'),
    (4, 0, 'Круговая 2')
]

# Объединяем все орбиты в один список
all_orbits = elliptical_orbits + other_orbits

# Рассчитываем высоты в перигее для всех орбит
heights_perigee = []
zr_radii = []
labels = []

for p, e, label in all_orbits:
    # Правильный масштаб для p: умножаем на 10000, чтобы получить реалистичные высоты
    p_km = p * 10000
    
    if e == 1:  # Параболическая орбита
        r_p = p_km / 2
        h_p = r_p - R_earth
        if h_p < 0:
            continue
    elif e > 1:  # Гиперболическая орбита
        a = p_km / (1 - e**2)  # a будет отрицательным
        r_p = a * (1 - e)      # r_p — положительное расстояние
        h_p = r_p - R_earth
        if h_p < 0:
            continue
    else:  # Эллиптическая или круговая орбита (e < 1)
        a = p_km / (1 - e**2)
        r_p = a * (1 - e)
        h_p = r_p - R_earth
        if h_p < 0:
            continue
    
    # Рассчитываем ЛИНЕЙНЫЙ радиус ЗР для этой высоты
    zr_radius = calculate_zr_radius(h_p)
    
    heights_perigee.append(h_p)
    zr_radii.append(zr_radius)
    labels.append(label)

# Преобразуем в массивы
heights_perigee = np.array(heights_perigee)
zr_radii = np.array(zr_radii)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(heights_perigee, zr_radii, marker='o', linestyle='-', linewidth=2, markersize=8)
plt.xlabel('Высота в перигее, h_p (км)')
plt.ylabel('Линейный радиус ЗР, ρ (км)')
plt.title('Зависимость линейного радиуса ЗР от высоты полета ИСЗ')
plt.grid(True)
plt.show()

# Вывод значений в консоль
print("\nЗависимость линейного радиуса ЗР от высоты:")
print("-" * 60)
for i, h in enumerate(heights_perigee):
    print(f"{labels[i]}: Высота h_p = {h:.2f} км -> Радиус ЗР ρ = {zr_radii[i]:.2f} км")