import numpy as np


def _validate(x, k):
    x = np.asarray(x, dtype=float)
    if x.ndim != 1:
        raise ValueError("signal must be 1-D")
    if x.size == 0:
        raise ValueError("signal is empty")
    if not np.all(np.isfinite(x)):
        raise ValueError("signal contains NaN or infinite values")
    if not isinstance(k, (int, np.integer)) or k < 0:
        raise ValueError("k must be a non-negative integer")
    return x


def mean_filter(x, k):
    """Running-mean filter with window size 2k+1, centred on each point.

    Near the edges the window shrinks to the available samples.
    Uses a cumulative sum.It runs in O(n) regardless of k.
    """
    x = _validate(x, k)
    n = x.size
    idx = np.arange(n)
    lo = np.clip(idx - k, 0, n)
    hi = np.clip(idx + k + 1, 0, n)
    csum = np.concatenate(([0.0], np.cumsum(x)))
    return (csum[hi] - csum[lo]) / (hi - lo)


def median_filter(x, k):
    """Running-median filter with window size 2k+1.

    Edges are handled by repeating the first/last sample.
    """
    x = _validate(x, k)
    if k == 0:
        return x.copy()
    padded = np.pad(x, k, mode="edge")
    windows = np.lib.stride_tricks.sliding_window_view(padded, 2 * k + 1)
    return np.median(windows, axis=1)


def despeckle(x, threshold, k=3, above=True):
    """Replace only the outliers with the local median.
    Points above or below the threshold are replaced by the
    median of their 2k+1 neighbourhood and every other point is left unchanged.
    """
    x = _validate(x, k)
    mask = x > threshold if above else x < threshold
    out = x.copy()
    out[mask] = median_filter(x, k)[mask]
    return out
