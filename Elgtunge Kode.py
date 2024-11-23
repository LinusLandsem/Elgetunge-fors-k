!pip install scipy

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

time_data = np.array([0, 2, 4, 6, 8, 10, 12, 14, 15, 20, 30, 40, 50])  #Tid
temp_data = np.array([99.6, 90, 83.5, 79.1, 75.2, 72.1, 69.4, 66.8, 65.6, 60.7, 53.4, 48.2, 44.7])  # Målt temperatur

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

