# Signal Denoising: Mean vs Median Filters

Two kinds of noise need two different filters.This project tests that on signals where the clean version is known and scores every result with RMSE and SNR improvement.

## Results

| Experiment | Result |
|---|---|
| Gaussian noise, running mean | Best window k = 86 cuts RMSE from 1.01 to 0.10 (+20.4 dB SNR). Larger windows flatten peaks and the error rises again. |
| Spike noise, mean filter | RMSE 19.8 → 6.5. The spikes are smeared, not removed. |
| Spike noise, median despeckle | RMSE 19.8 → 0.011. Only flagged outliers are replaced; all other samples are untouched. |
| EKG recording | Median step fixes 5 dropout samples (RMSE 123.8 → 100.9); a light running mean (k = 5) brings it to 40.5 (+9.7 dB SNR). The filter lowers the sharp R-peaks slightly, which is the cost of averaging. |

See [`denoising.ipynb`](denoising.ipynb) for the plots and the full walkthrough.

## Files

```
filters.py        mean_filter, median_filter, despeckle
metrics.py        rmse, correlation, snr_db, snr_improvement_db
denoising.ipynb   the experiments
data/             EKG_signals.csv
```

## Notes

- The mean filter uses a cumulative sum and the median filter uses sliding windows.
- Input is validated (empty, NaN/inf, non-1-D, invalid window size).
- Edges: the mean filter shrinks its window and the median filter repeats the edge sample.
- despeckle replaces only points past a threshold .So clean samples are never altered.

