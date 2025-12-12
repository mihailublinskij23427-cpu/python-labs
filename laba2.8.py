import numpy as np
import matplotlib.pyplot as plt

# Параметры
N = 500
mean_noise = 2
std_noise = 2
amplitudes = [11, 2, 1, 7]
frequencies = [0.5, 0.4, 1, 2]

# Генерация оси x (время или индекс)
x = np.linspace(0, 2 * np.pi, N)

# Генерация шума (нормальное распределение)
noise = np.random.normal(mean_noise, std_noise, N)

# Генерация суммы синусоид
signal = np.zeros(N)
for amp, freq in zip(amplitudes, frequencies):
    signal += amp * np.sin(2 * np.pi * freq * x)

# Аддитивная смесь: сигнал + шум
additive_mixture = signal + noise

# Мультипликативная смесь: сигнал × шум
multiplicative_mixture = signal * noise

# Функция для вычисления амплитудного спектра
def get_amplitude_spectrum(data, fs=100):
    fft_result = np.fft.fft(data)
    freqs = np.fft.fftfreq(len(data), 1/fs)
    half = len(data) // 2
    return freqs[:half], np.abs(fft_result[:half])

# Вычисляем спектры
fs = 100  # Условная частота дискретизации

freqs_signal, spec_signal = get_amplitude_spectrum(signal, fs)
freqs_noise, spec_noise = get_amplitude_spectrum(noise, fs)
freqs_add, spec_add = get_amplitude_spectrum(additive_mixture, fs)
freqs_mult, spec_mult = get_amplitude_spectrum(multiplicative_mixture, fs)

# Вывод графиков

# Графики временных реализаций
plt.figure(figsize=(14, 10))

plt.subplot(4, 2, 1)
plt.plot(noise, label='Шум', color='blue')
plt.title('Нормальный шум (μ=2, σ=2)')
plt.grid(True)
plt.legend()

plt.subplot(4, 2, 2)
plt.plot(signal, label='Сигнал (сумма синусоид)', color='orange')
plt.title('Сумма 4 синусоид')
plt.grid(True)
plt.legend()

plt.subplot(4, 2, 3)
plt.plot(additive_mixture, label='Аддитивная смесь', color='green')
plt.title('Сигнал + Шум')
plt.grid(True)
plt.legend()

plt.subplot(4, 2, 4)
plt.plot(multiplicative_mixture, label='Мультипликативная смесь', color='red')
plt.title('Сигнал × Шум')
plt.grid(True)
plt.legend()

# Графики амплитудных спектров
plt.subplot(4, 2, 5)
plt.plot(freqs_signal, spec_signal, label='Спектр сигнала', color='orange')
plt.title('Амплитудный спектр сигнала')
plt.grid(True)
plt.legend()

plt.subplot(4, 2, 6)
plt.plot(freqs_noise, spec_noise, label='Спектр шума', color='blue')
plt.title('Амплитудный спектр шума')
plt.grid(True)
plt.legend()

plt.subplot(4, 2, 7)
plt.plot(freqs_add, spec_add, label='Спектр аддитивной смеси', color='green')
plt.title('Амплитудный спектр аддитивной смеси')
plt.grid(True)
plt.legend()

plt.subplot(4, 2, 8)
plt.plot(freqs_mult, spec_mult, label='Спектр мультипликативной смеси', color='red')
plt.title('Амплитудный спектр мультипликативной смеси')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()