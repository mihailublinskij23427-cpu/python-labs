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
freqs_half = freqs_full[:N//2]        # Только положительные частоты

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

# Амплитудный спектр отфильтрованного сигнала (только положительные частоты)
filtered_magnitude = np.abs(filtered_spectrum[:N//2])

# Вывод графиков
plt.figure(figsize=(14, 8))

# 1. Исходный амплитудный спектр
plt.subplot(2, 2, 1)
plt.plot(freqs_half, np.abs(fft_result[:N//2]), label='Исходный спектр', color='blue')
plt.title('Исходный амплитудный спектр')
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()

# 2. АЧХ фильтра
plt.subplot(2, 2, 2)
plt.plot(freqs_full, a4h, label='АЧХ фильтра', color='orange')
plt.title(f'Прямоугольная АЧХ фильтра\nрезонансная частота={freq_rez} Гц, полоса={polosa} Гц')
plt.xlabel('Частота (Гц)')
plt.ylabel('Коэффициент передачи')
plt.grid(True)
plt.legend()

# 3. Отфильтрованный спектр
plt.subplot(2, 2, 3)
plt.plot(freqs_half, filtered_magnitude, label='Отфильтрованный спектр', color='green')
plt.title('Амплитудный спектр после фильтрации')
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()

# 4. Временная реализация: исходная смесь vs отфильтрованная
plt.subplot(2, 2, 4)
plt.plot(t, additive_mixture, label='Исходная смесь', color='red', alpha=0.5)
plt.plot(t, np.real(np.fft.ifft(filtered_spectrum)), label='Отфильтрованная смесь', color='blue')
plt.title('Временная реализация: исходная vs отфильтрованная')
plt.xlabel('Время / Индекс')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()