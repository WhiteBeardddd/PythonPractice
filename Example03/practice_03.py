import numpy as np
import matplotlib.pyplot as plt

fs = 8000
dur = 0.5
f = 3500
point = 50

N = int(fs * dur)
n = np.arange(N)
x = np.sin(2 * np.pi * f * n / fs)

plt.figure(figsize=(10, 4))
plt.plot(n[:point], x[:point])

plt.title("440 Hz Sine (first 100 samples)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

plt.show()
