import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Grid creating
Kp = np.linspace(0.1, 10, 400)
ki_values = np.linspace(0.1, 10, 10)  # set Ki
colors = cm.plasma(np.linspace(0, 1, len(ki_values)))  # set the color for each Ki

plt.figure(figsize=(12, 10))

for ki, color in zip(ki_values, colors):
    Kd = ki / Kp # calculate Kd
    plt.plot(Kp, Kd, label=f'Ki = {ki:.1f}', color=color)

plt.xlabel('Kp')
plt.ylabel('Kd')
plt.title('Curves of Kp * Kd = Ki for different Ki values')
plt.legend(title="Ki values")
plt.ylim(0, 10)  # restrict the range of Kd
plt.grid(True)
plt.show()