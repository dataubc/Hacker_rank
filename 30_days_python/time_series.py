# Enter your code here. Read input from STDIN. Print output to STDOUT
import pandas as pd
import numpy as np
import pylab as pl
from numpy import fft


def fourierExtrapolation(x, n_predict):
    n = x.size
    n_harm = 10  # number of harmonics in model
    t = np.arange(0, n)
    p = np.polyfit(t, x, 1)  # find linear trend in x
    x_notrend = x - p[0] * t  # detrended x
    x_freqdom = fft.fft(x_notrend)  # detrended x in frequency domain
    f = fft.fftfreq(n)  # frequencies
    # sort indexes by frequency, lower -> higher

    indexes = list(range(n))
    t = np.arange(0, n + n_predict)
    restored_sig = np.zeros(t.size)
    for i in indexes[:1 + n_harm * 2]:
        ampli = np.absolute(x_freqdom[i]) / n  # amplitude
        phase = np.angle(x_freqdom[i])  # phase
        restored_sig += ampli * np.cos(2 * np.pi * f[i] * t + phase)
    return restored_sig + p[0] * t


def main():
    df = pd.read_fwf('hacker_rack/input/input01.txt')
    x = df.to_numpy().ravel()

    n_predict = 30
    extrapolation = fourierExtrapolation(x, n_predict)
    print(extrapolation)
    pl.plot(np.arange(0, extrapolation.size), extrapolation, 'r', label='extrapolation')
    pl.plot(np.arange(0, x.size), x, 'b', label='x', linewidth=3)
    pl.legend()
    pl.show()


if __name__ == "__main__":
    main()