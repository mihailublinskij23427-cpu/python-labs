import numpy as np
import matplotlib.pyplot as plt

# Параметры
N = 500           # Длина массива
amplitudes = [11, 2, 1, 7]
frequencies = [0.5, 0.4, 1, 2]
mean_noise = 2    # Математическое ожидание шума
std_noise = 2     # СКО шума

# Генерация оси времени
t = np.linspace(0, 2 * np.pi, N)  # Временная ось

# Генерация суммы синусоид
signal = np.zeros(N)
for amp, freq in zip(amplitudes, frequencies):
    signal += amp * np.sin(2 * np.pi * freq * t)

# Генерация белого гауссова шума (БГШ)
noise = np.random.normal(mean_noise, std_noise, N)

# Аддитивная смесь: сигнал + шум
additive_mixture = signal + noise

# Прямое преобразование Фурье для аддитивной смеси
fft_result = np.fft.fft(additive_mixture)

# Частотная шкала
fs = 100  # Условная частота дискретизации (для масштаба)
freqs_full = np.fft.fftfreq(N, 1/fs)  # Полная шкала (отрицательные и положительные частоты)

# Параметры фильтра
freq_rez = 1   # Резонансная частота (Гц)
polosa = 1     # Полоса пропускания (Гц)

# Границы полосы пропускания
min_freq = freq_rez - polosa / 2
max_freq = freq_rez + polosa / 2

# Создание прямоугольной АЧХ фильтра (в полной шкале)
a4h = np.zeros(N)
for i in range(N):
    if min_freq <= freqs_full[i] <= max_freq:
        a4h[i] = 1

# Перемножение спектра на АЧХ
filtered_spectrum = fft_result * a4h

# Обратное преобразование Фурье — получаем отфильтрованный сигнал во временной области
filtered_signal = np.real(np.fft.ifft(filtered_spectrum))

# Вывод графиков
plt.figure(figsize=(14, 8))

# 1. Исходная аддитивная смесь (временная область)
plt.subplot(2, 2, 1)
plt.plot(t, additive_mixture, label='Исходная аддитивная смесь', color='red', alpha=0.7)
plt.title('Исходная аддитивная смесь')
plt.xlabel('Время / Индекс')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()

# 2. Исходный амплитудный спектр
plt.subplot(2, 2, 2)
plt.plot(freqs_full[:N//2], np.abs(fft_result[:N//2]), label='Исходный спектр', color='blue')
plt.title('Исходный амплитудный спектр')
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()

# 3. Отфильтрованный амплитудный спектр
plt.subplot(2, 2, 3)
plt.plot(freqs_full[:N//2], np.abs(filtered_spectrum[:N//2]), label='Отфильтрованный спектр', color='green')
plt.title('Амплитудный спектр после фильтрации')
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()

# 4. Сравнение: исходная смесь vs отфильтрованный сигнал (временная область)
plt.subplot(2, 2, 4)
plt.plot(t, filtered_signal, label='Отфильтрованный сигнал', color='blue')
plt.plot(t, additive_mixture, label='Исходная смесь', color='red', alpha=0.5)
plt.title('Сравнение: исходная vs отфильтрованная')
plt.xlabel('Время / Индекс')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()