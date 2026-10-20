"""Metrics for comparing a filtered signal with a known clean signal."""
import numpy as np


def _pair(clean, other):
    clean, other = np.asarray(clean, float), np.asarray(other, float)
    if clean.shape != other.shape:
        raise ValueError("signals must have the same shape")
    return clean, other


def rmse(clean, other):
    clean, other = _pair(clean, other)
    return float(np.sqrt(np.mean((clean - other) ** 2)))


def correlation(clean, other):
    clean, other = _pair(clean, other)
    return float(np.corrcoef(clean, other)[0, 1])


def snr_db(clean, other):
    """Signal-to-noise ratio""" 
    clean, other = _pair(clean, other)
    noise_power = np.mean((other - clean) ** 2)
    if noise_power == 0:
        return float("inf")
    return float(10 * np.log10(np.mean(clean ** 2) / noise_power))


def snr_improvement_db(clean, noisy, filtered):
    """How many dB the filter improved the SNR."""
    return snr_db(clean, filtered) - snr_db(clean, noisy)
