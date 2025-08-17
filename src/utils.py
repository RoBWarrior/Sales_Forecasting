# src/utils.py
import matplotlib.pyplot as plt

def save_plot(fig, filename):
    """Save matplotlib figure."""
    fig.savefig(f"visuals/{filename}", bbox_inches='tight')
    print(f"Plot saved to visuals/{filename}")
