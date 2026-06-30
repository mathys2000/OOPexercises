# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: Python [conda env:ecen3300]
#     language: python
#     name: conda-env-ecen3300-py
# ---

# %% [markdown]
# # Exercise 1
#
# Exercise 1: Build a Signal object

# %%
import numpy as np
import matplotlib.pyplot as plt


# %%
class Signal:
    """
    Pseudo continuous-time x(t) signal object with time axis tt.
    x(t) is assumed to be sampled uniformly with sampling rate fs.
    """

    def __init__(self, tt, xt):
        if len(tt) != len(xt):
            raise ValueError("tt and xt must have the same length")
        self.tt = np.array(tt)
        dt = np.diff(self.tt)
        if not np.allclose(dt, dt[0]):
            raise ValueError("time samples must be uniformly spaced")
        self.xt = np.array(xt)
        self.fs = (self.tt.size-1)/(self.tt[-1]-self.tt[0])

    def duration(self):
        return self.tt.size/self.fs

    def energy(self):
        return np.sum(np.abs(self.xt)**2)/self.fs

    def plot(self):

        fig = plt.figure()
        ax1, ax2 = fig.subplots(2, 1, sharex=True)
        ax1.plot(self.tt, np.real(self.xt), '-b')
        ax1.set_ylabel('Re[x(t)]')
        ax1.grid(alpha=0.6)
        ax1.set_title(f'Signal $x(t)$, $f_s$={self.fs:.1f} Hz')
        ax2.plot(self.tt, np.imag(self.xt), '-r')
        ax2.set_ylabel('Im[x(t)]')
        ax2.set_xlabel('t [sec]')
        ax2.grid(alpha=0.6)

        plt.show()


# %%
fs = 100
tlen = 1
tt = np.arange(int(np.round(tlen*fs)))/fs
A1, f1, th1 = 2, 1.6, -90
x1t = Signal(tt, A1*np.exp(1j*(2*np.pi*f1*tt+np.pi/180*th1)))

# %%
print(x1t.fs)
print(x1t.duration())
print(x1t.energy())

# %%
x1t.plot()

# %% [markdown]
# **Thinking exercise**
#
# * Why is fs stored?
# * Why is energy() inside the object?
# * Should plotting belong here?
# * What should remain external?
#
# **Answers**
#
# * fs relates the samples xt to the time axis.
# * Energy is a property of the signal xt.
# * A plot of signal xt is another representation of the signal. It is debatable whether that should be done internally or externally.
# * The use of this signal in a larger system, e.g., an AM communication system.
#
# ---
#

# %%
