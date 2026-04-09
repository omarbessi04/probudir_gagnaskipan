import numpy as np
import matplotlib.pyplot as plt
import math
import os

output_dir = "complexity_plots"
os.makedirs(output_dir, exist_ok=True)

N = np.linspace(1, 100, 500)

complexities = [
    ("O(n)", N, "#f28e2b"),
    ("O(log n)", np.log2(N), "#4e79a7"),
    ("O(n²)", N**2, "#e15759"),
    ("O(n log n)", N * np.log2(N), "#59a14f"),
    ("O(n³)", N**3, "#b07aa1"),
    ("O(2ⁿ)", np.minimum(2**N, 1e8), "#76b7b2"),
]

fig, ax = plt.subplots(figsize=(10, 6))

for i, (label, y, color) in enumerate(complexities):
    ax.plot(N, y, label=label, color=color, linewidth=2.5)

    ax.set_xlim(1, 100)
    ax.set_ylim(0, min(ax.get_ylim()[1], 1e6))

    # Dynamically scale y-axis to visible curves only
    visible_ys = [complexities[j][1] for j in range(i + 1)]
    max_visible = max(np.max(y_vals[N <= 100]) for y_vals in visible_ys)
    ax.set_ylim(0, min(max_visible * 1.1, 1e8))

    ax.set_xlabel("Input size (n)", fontsize=13)
    ax.set_ylabel("Operations", fontsize=13)
    ax.set_title("Time Complexity Comparison", fontsize=15, fontweight="bold")
    ax.legend(loc="upper left", fontsize=11)
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.tick_params(labelsize=11)

    filename = os.path.join(
        output_dir,
        f"step_{i + 1:02d}_{label.replace('(', '').replace(')', '').replace(' ', '_').replace('²', '2').replace('³', '3').replace('ⁿ', 'n')}.png",
    )
    fig.savefig(filename, dpi=150, bbox_inches="tight")
    print(f"Saved: {filename}")

plt.close(fig)
print("\nAll plots saved to:", output_dir)
