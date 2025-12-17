import numpy as np
import matplotlib.pyplot as plt
import os

# 1. Data generation with NumPy
# Create an array of 1000 points between 0 and 2*pi
x = np.linspace(0, 2 * np.pi, 1000)

# Compute the sine of each point
y = np.sin(x)

# 2. Visualization with Matplotlib
plt.figure(figsize=(8, 5))

# Plot the sine function
plt.plot(x, y, label='sin(x)', linewidth=2)

plt.title('Simple Sine Function', fontsize=14)
plt.xlabel('Angle (radians)', fontsize=10)
plt.ylabel('Amplitude', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper right')

plt.annotate(
    'Maximum Peak',
    xy=(np.pi / 2, 1),
    xytext=(np.pi / 2 + 0.5, 0.8),
    arrowprops=dict(facecolor='black', shrink=0.05)
)

output_filename = os.path.join(os.path.dirname(__file__), 'sine_wave.png')
plt.savefig(output_filename)
print(f"Chart saved at: {output_filename}")
# plt.show()
