!pip install scipy

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

time_data = np.array([0, 1, 2, 3, 4, 5, 10, 15, 20])  #Tid
temp_data = np.array([90, 85, 80, 76, 73, 70, 60, 55, 52])  # Målt temperatur

T_K = 20  # Omgivelsestemperatur (°C)

def avkjølings_modell(t, alpha):
    T_0 = temp_data[0]  # Starttemperatur
    return T_K + (T_0 - T_K) * np.exp(-alpha * t)

popt, _ = curve_fit(avkjølings_modell, time_data, temp_data)
alpha_opt = popt[0]  # Optimal verdi for alpha

time_fit = np.linspace(0, max(time_data), 100)
temp_fit = avkjølings_modell(time_fit, alpha_opt)

plt.plot(time_data, temp_data, 'o-', label='Eksperimentelle verdier')  # Målte temperaturer
plt.plot(time_fit, temp_fit, '-', label=f'Teoretisk modell ($\\alpha$={alpha_opt:.4f})')  # Modell
plt.axhline(y=T_K, color='gray', linestyle='--', label='Omgivelsestemperatur')  # Omgivelsestemperatur

plt.xlabel('Tid (minutter)')
plt.ylabel('Temperatur (°C)')
plt.legend()
plt.title("Newtons avkjølingslov: Eksperiment vs Modell")
plt.grid()
plt.show()

print(f"Optimal verdi for alpha: {alpha_opt:.4f}")
