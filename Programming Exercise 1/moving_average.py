import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import dlti, dimpulse

def moving_average_system(order: int):
    """
    Create a discrete-time moving average system of given order.
    
    Parameters:
        order (int): Number of samples to average.
    
    Returns:
        dlti system: Discrete LTI system object.
    """
    b = np.ones(order) / order   # numerator coefficients (FIR averaging filter)
    a = [1.0]                    # denominator coefficients (no feedback, FIR)
    return dlti(b, a)

def plot_impulse_response(order: int, n: int = 15, ax=None):
    """
    Plot the impulse response of a moving average system.
    
    Parameters:
        order (int): Moving average filter order.
        n (int): Number of samples for impulse response.
        ax: Optional matplotlib axis to plot on.
    """
    system = moving_average_system(order)
    t, h = dimpulse(system, n=n)
    t = np.squeeze(t)
    h = np.squeeze(h)

    if ax is None:
        fig, ax = plt.subplots()
    ax.stem(t, h, use_line_collection=True)
    ax.set_xlabel("n (samples)")
    ax.set_ylabel("h[n]")
    ax.set_title(f"Impulse Response (MA Order {order})")
    ax.grid(True)

# --- Test Cases ---
orders = [3, 5, 7]  # Try moving averages of different lengths
n_samples = 15

fig, axes = plt.subplots(1, len(orders), figsize=(12, 4))
for i, order in enumerate(orders):
    plot_impulse_response(order, n=n_samples, ax=axes[i])

plt.tight_layout()
plt.show()
