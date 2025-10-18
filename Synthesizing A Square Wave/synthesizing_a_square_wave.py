import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 4 * np.pi, 1000)
y = np.zeros_like(t)

num_harmonics = 10

for i in range(num_harmonics):
    k = 2 * i + 1
    y += (4 / (k * np.pi)) * np.sin(k * t)
    

plt.plot(t, y)
plt.title(f'Square Wave Synthesis ({num_harmonics} terms)')
plt.show()