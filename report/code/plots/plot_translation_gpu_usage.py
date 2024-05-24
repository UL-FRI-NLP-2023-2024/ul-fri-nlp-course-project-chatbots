import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
labels = ["FT", "PT", "LoRa", "LoHa"]
gpu_memory_1 = [6.4, 4.6, 8.2, 6.0]

# Bar width
bar_width = 1

# Positions of the bars on the x-axis
r1 = np.arange(len(labels))

# Create the plot
fig, ax = plt.subplots(figsize=(10, 5))

ax.grid(axis='y', linestyle='--', linewidth=0.7, zorder=0)
bars = ax.bar(r1, gpu_memory_1, color=['#b056d1', '#ef925e', '#f3b864', '#5a7df4'], width=bar_width, zorder=3)

for i in range(len(r1)):
    ax.text(r1[i], gpu_memory_1[i] , str(gpu_memory_1[i]), ha='center', va='bottom', rotation=45, fontsize=10, fontweight='bold')

ax.set_xticks(r1)
ax.set_xticklabels(labels)
ax.set_title('Machine Translation (slovenian to english)', fontsize=14)
ax.set_ylabel('GPU memory (GB)', fontsize=12)

plt.show()