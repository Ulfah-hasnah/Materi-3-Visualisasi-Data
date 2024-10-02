import numpy as np
import matplotlib.pyplot as plt

# Diketahui
V0 = 0
g = 9.8  # Percepatan gravitasi (m/s^2)
h0 = 100  # Ketinggian awal benda (misalnya 100 meter)

# Waktu yang diperlukan untuk mencapai tanah
t_max = np.sqrt((2 * h0) / g)
print(f"Waktu yang diperlukan benda untuk mencapai tanah: {t_max:.2f} detik")

# Kecepatan sebagai fungsi waktu v(t) = g * t
t = np.linspace(0, t_max, 500)  # Waktu dari 0 hingga t_max dengan 500 titik
v = g * t  # Kecepatan sebagai fungsi waktu

# Posisi (ketinggian) sebagai fungsi waktu h(t) = h0 - 1/2 * g * t^2
h = h0 - 0.5 * g * t**2

# Plotting grafik kecepatan
plt.figure()
plt.plot(t, v, label='Kecepatan (v)')
plt.title('Grafik Kecepatan Benda sebagai Fungsi Waktu')
plt.xlabel('Waktu (detik)')
plt.ylabel('Kecepatan (m/s)')
plt.grid(True)
plt.legend()

# Plotting grafik posisi
plt.figure()
plt.plot(t, h, label='Posisi (h)', color='orange')
plt.title('Grafik Posisi (Ketinggian) Benda sebagai Fungsi Waktu')
plt.xlabel('Waktu (detik)')
plt.ylabel('Ketinggian (m)')
plt.grid(True)
plt.legend()

plt.show()
