import numpy as np
import matplotlib.pyplot as plt

def plot_impulse_response(order: int, n: int = 15, ax=None):
    """
    Plot the impulse response of a moving average filter directly.
    
    Parameters:
        order (int): Number of samples to average.
        n (int): Total number of samples to plot.
        ax: Optional matplotlib axis.
    """
    h = np.zeros(n)
    h[:order] = 1 / order  # first 'order' samples are 1/order
    t = np.arange(n)

    if ax is None:
        fig, ax = plt.subplots()
    ax.stem(t, h)  # works in any Matplotlib version
    ax.set_xlabel("n (samples)")
    ax.set_ylabel("h[n]")
    ax.set_title(f"Impulse Response (MA Order {order})")
    ax.grid(True)

# --- Test Cases ---
orders = [3, 5, 7]
n_samples = 15

fig, axes = plt.subplots(1, len(orders), figsize=(12, 4))
for i, order in enumerate(orders):
    plot_impulse_response(order, n=n_samples, ax=axes[i])

plt.tight_layout()
plt.show()
