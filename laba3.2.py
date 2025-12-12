import numpy as np
import matplotlib.pyplot as plt

# Параметры сигнала
amplitude = 11
frequency = 0.5   # Гц
N = 500           # Длина массива

# Генерация оси времени
t = np.linspace(0, 2 * np.pi, N)  # Временная ось

# Генерация синусоидального сигнала
signal = amplitude * np.sin(2 * np.pi * frequency * t)

# Прямое преобразование Фурье
fft_result = np.fft.fft(signal)

# Частотная шкала
fs = 100  # Условная частота дискретизации
freqs = np.fft.fftfreq(N, 1/fs)

# Берём только первую половину спектра (для вещественных сигналов)
half_N = N // 2
freqs = freqs[:half_N]
fft_magnitude = np.abs(fft_result[:half_N])

# Вывод графиков
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal, label='Сигнал', color='blue')
plt.title(f'Временная реализация: sin(2π·{frequency}·t), A={amplitude}')
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