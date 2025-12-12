import numpy as np
import matplotlib.pyplot as plt

# Параметры
N = 500
mean_noise = 2
std_noise = 2
amplitudes = [11, 2, 1, 7]
frequencies = [0.5, 0.4, 1, 2]

# Генерация шума (нормальное распределение)
noise = np.random.normal(mean_noise, std_noise, N)

# Генерация оси x (время или индекс)
x = np.linspace(0, 2 * np.pi, N)

# Генерация суммы синусоид
signal = np.zeros(N)
for amp, freq in zip(amplitudes, frequencies):
    signal += amp * np.sin(2 * np.pi * freq * x)

# Аддитивная смесь
mixed_signal = signal + noise

# Вывод графиков
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(noise, label='Шум')
plt.title('Нормальный шум (μ=2, σ=2)')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(signal, label='Сигнал (сумма синусоид)', color='orange')
plt.title('Сумма 4 синусоид')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(mixed_signal, label='Аддитивная смесь', color='green')
plt.title('Аддитивная смесь сигнала и шума')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()