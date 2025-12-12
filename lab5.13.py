import numpy as np
import matplotlib.pyplot as plt

# Принимаем радиус Земли в километрах
R_earth = 6371.0  # км

# Функция для расчета ЛИНЕЙНОГО радиуса ЗР (в км) по высоте h и β_min
def calculate_zr_radius(h, beta_min_deg):
    beta_min_rad = np.deg2rad(beta_min_deg)
    # Центральный угол θ (в радианах)
    theta_rad = np.arccos(R_earth * np.cos(beta_min_rad) / (R_earth + h))
    # Линейный радиус ЗР = R_earth * θ
    zr_radius_km = R_earth * theta_rad
    return zr_radius_km

# Массив высот для построения графика (от 0 до 50000 км)
heights = np.linspace(0, 50000, 200)

# Массив значений β_min (в градусах)
beta_min_values = [10, 20, 30, 35, 40]

# Создаем фигуру
plt.figure(figsize=(10, 6))

# Цикл по разным значениям β_min
for beta_min in beta_min_values:
    zr_radii = calculate_zr_radius(heights, beta_min)
    plt.plot(heights, zr_radii, label=f'β_min = {beta_min}°')

# Настройки графика
plt.xlabel('Высота полета, h (км)')
plt.ylabel('Линейный радиус ЗР, ρ (км)')
plt.title('Семейство зависимостей размера ЗР от высоты для разных β_min')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()