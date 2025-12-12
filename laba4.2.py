import numpy as np
import matplotlib.pyplot as plt

# Параметры
N = 500           # Длина массива
amplitudes = [11, 2, 1, 7]
frequencies = [0.5, 0.4, 1, 2]

# Генерация оси времени
t = np.linspace(0, 2 * np.pi, N)  # Временная ось

# Генерация суммы синусоид
signal = np.zeros(N)
for amp, freq in zip(amplitudes, frequencies):
    signal += amp * np.sin(2 * np.pi * freq * t)

# Прямое преобразование Фурье
fft_result = np.fft.fft(signal)

# Частотная шкала
fs = 100  # Условная частота дискретизации (для масштаба)
freqs = np.fft.fftfreq(N, 1/fs)

# Берём только первую половину спектра (из-за симметрии для вещественных сигналов)
half_N = N // 2
freqs = freqs[:half_N]
fft_magnitude = np.abs(fft_result[:half_N])

# Вывод графиков
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal, label='Сумма синусоид', color='blue')
plt.title('Временная реализация: сумма 4 синусоид')
plt.xlabel('Время / Индекс')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(freqs, fft_magnitude, label='Амплитудный спектр', color='orange')
plt.title('Частотная реализация (амплитудный спектр)')
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()