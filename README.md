# EKG Signal Denoising Using Python

## Project Overview

This project explores basic signal-denoising techniques using Python. The initial experiments was performed on synthetically generated signals with controlled noise to understand how simple filtering approaches affect noisy data.

The filtering techniques were then applied to biomedical EKG data to observe their effectiveness in reducing visible noise while comparing the processed signals with corresponding original signals.

This was an exploratory learning project focused on gaining practical exposure to basic signal processing and working with real-world biomedical signal data.

## Objective

The objective of the project was to experiment with simple signal-smoothing and noise-reduction techniques and understand how different filtering approaches affect the appearance of a noisy signal.

The project also provided an opportunity to apply the techniques developed on synthetic data to biomedical EKG signals.

## Tools & Technologies

- Python
- NumPy
- Pandas
- Matplotlib
- Basic signal processing
- Jupyter Notebook

## Approach

The project was developed in two stages.

### 1. Experiments with Synthetic Signals

Synthetic signals were generated and controlled amounts of noise were introduced to study the behavior of basic filtering techniques.

Different smoothing-window sizes were experimented with to observe their effect on the resulting signal.

### 2. Biomedical EKG Signal Processing

The filtering approaches were then applied to biomedical EKG data containing noisy and corresponding original signal values.

The noisy portions of the EKG signal were processed using median filtering and mean-based smoothing. The resulting signals were plotted and compared with the corresponding original EKG data to visually observe the effect of noise reduction.

## Results

The experiments showed that basic smoothing and median-filtering approaches could reduce certain types of noise and produce cleaner signal representations.

The experiments also demonstrated that the choice of filtering approach and smoothing window can affect the resulting signal, providing practical exposure to the trade-offs involved in basic signal processing.

## Key Learning

Through this project, I gained practical experience with:

- Generating and working with synthetic noisy signals
- Applying basic signal-smoothing techniques using Python
- Experimenting with different smoothing-window sizes
- Applying median filtering to noisy signal data
- Working with biomedical EKG data
- Comparing processed signals with corresponding original signals
- Visualizing signal-processing results using Matplotlib

## Limitations

This project was an introductory exploration of basic signal-denoising techniques. It was not intended to implement an advanced EKG signal-processing system.

More advanced signal-processing methods could be explored as a future extension of the project.

