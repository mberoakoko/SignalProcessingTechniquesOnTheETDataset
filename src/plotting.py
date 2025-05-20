from matplotlib.figure import Figure
from matplotlib.axes import Axes
import matplotlib.pyplot as plt
from src.signal_generator import SinusoidSignal

plt.style.use("bmh")
plt.rcParams.update(
    {
        "font.size": 7,
        "figure.dpi": 200
    }
)


def plot_sinusidal_signal(sinusidal_signal: SinusoidSignal) -> None:
    fig: Figure = plt.figure(figsize=(16//2, 9//2))
    ax: Axes = fig.add_subplot(211)
    ax.plot(sinusidal_signal.t, sinusidal_signal.x, color="C1",
            label="Sinusidal Signal", linewidth=0.7)
    ax.legend()
    plt.title("Simple signal")
    plt.tight_layout()
    plt.show()