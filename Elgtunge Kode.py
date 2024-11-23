import numpy as np
import matplotlib.pyplot as plt

time_data = [0, 1, 2, 3, 4, 5, 10, 15, 20]
temp_data = [90, 85, 80, 76, 73, 70, 60, 55, 52]

T_K = 21  # Romtemperatur (°C)
T_0 = temp_data[0]  # Starttemperatur

alpha = 0.1

# Teoretisk temperatur med Newtons avkjølingslov
time_fit = np.linspace(0, max(time_data), 100)
temp_fit = T_K + (T_0 - T_K) * np.exp(-alpha * time_fit)

plt.plot(time_data, temp_data, 'o', label='Målte data')
plt.plot(time_fit, temp_fit, '-', label=f'Teoretisk modell ($\\alpha$={alpha})')
plt.axhline(y=T_K, color='gray', linestyle='--', label='Omgivelsestemperatur')
plt.xlabel('Tid (minutter)')
plt.ylabel('Temperatur (°C)')
plt.legend()
plt.title("Newtons avkjølingslov")
plt.grid()
plt.show()
