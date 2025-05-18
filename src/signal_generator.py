import numpy as np
from typing import NamedTuple

RNG = np.random.default_rng(2000)


class SinusoidSignal(NamedTuple):
    t: np.ndarray
    x: np.ndarray


def generate_test_signal(omega_1: float, omega_2: float, f_s: float, with_noise: bool = False,
                         t_final: float = 10) -> SinusoidSignal:
    dt = 1 / f_s
    t: np.ndarray = np.linspace(0, t_final, round(t_final / dt))
    return SinusoidSignal(
        t,
        x=np.sin(2 * np.pi * omega_1 * t) + np.sin(2 * np.pi * omega_2 * t) + with_noise * RNG.normal(0, scale=1,
                                                                                                      size=t.shape)
    )
