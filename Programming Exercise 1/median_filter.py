import matplotlib.pyplot as plt
from statistics import median

# --- Median Filter Function ---
def median_filter(x):
    y = []
    for n in range(len(x)):
        if n == 0:
            window = [x[n], x[n], x[n+1]]
        elif n == len(x)-1:
            window = [x[n-1], x[n], x[n]]
        else:
            window = [x[n-1], x[n], x[n+1]]
        y.append(median(window))
    return y

# --- Test signals ---
x1 = [0, 0, 100, 0, 0]
x2 = [0, 1, 0, 0, 0]

# Apply median filter
Sx1 = median_filter(x1)
Sx2 = median_filter(x2)
Sx1_plus_x2 = median_filter([a+b for a, b in zip(x1, x2)])
Sx1_plus_Sx2 = [a+b for a, b in zip(Sx1, Sx2)]

# --- Print results ---
print("S(x1)      =", Sx1)
print("S(x2)      =", Sx2)
print("S(x1+x2)   =", Sx1_plus_x2)
print("S(x1)+S(x2)=", Sx1_plus_Sx2)

# --- Plot ---
plt.figure(figsize=(10, 6))
n = range(len(x1))

plt.stem(n, x1, linefmt='C0-', markerfmt='C0o', basefmt=" ", label='x1')
plt.stem(n, x2, linefmt='C1-', markerfmt='C1s', basefmt=" ", label='x2')
plt.stem(n, Sx1, linefmt='C2--', markerfmt='C2^', basefmt=" ", label='S(x1)')
plt.stem(n, Sx2, linefmt='C3--', markerfmt='C3v', basefmt=" ", label='S(x2)')
plt.stem(n, Sx1_plus_x2, linefmt='C4-.', markerfmt='C4D', basefmt=" ", label='S(x1+x2)')
plt.stem(n, Sx1_plus_Sx2, linefmt='C5-.', markerfmt='C5d', basefmt=" ", label='S(x1)+S(x2)')

plt.xlabel('n (samples)')
plt.ylabel('Amplitude')
plt.title('Median Filter Response')
plt.legend()
plt.grid(True)
plt.show()
