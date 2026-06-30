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
# # Critique for Exercise 2c
#
# Response from ChatGPT-5.5 Pro to jupyter notebook file Exercise 2c.ipynb, 5-28-26 

# %% [markdown]
# Yes — this is a **clear improvement** over Exercise 2b.
#
# ### Good parts
#
# | Aspect                                            | Comment                                                                                                          |
# | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
# | `Oscilloscope.load_signal(signal)` is much better | The scope now receives a `Signal` object instead of disconnected `xt` and `fs`. This is the biggest improvement. |
# | Better ownership model                            | `Signal` owns `tt`, `xt`, and `fs`; `Oscilloscope` owns display state. Good OOP design.                          |
# | Time-scale behavior improved                      | The scope now clips the displayed signal to the requested time window.                                           |
# | Good error checks                                 | Missing-signal checks in `autoscale()`, `measure_rms()`, and `display()` are appropriate.                        |
# | Independent scopes                                | The examples with `scope1` and `scope2` show separate object state well.                                         |
#
# ### Weak parts
#
# | Issue                                                           | Comment                                                                                                       |
# | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
# | `current_signal_orig` and `time_orig` should be listed as state | The notebook answer omits them, but they are part of the object’s persistent state.                           |
# | `find_time_overlap()` mutates its argument                      | It changes `t_scale[0]` and `t_scale[1]` before returning. Better to create a new list instead.               |
# | Invalid scale input is silently ignored                         | In `__init__`, if `voltage_scale` has the wrong length, nothing happens. Better to raise `ValueError`.        |
# | `autoscale()` uses displayed signal but checks original signal  | It should check `self.current_signal is None`, since that is what it actually scales.                         |
# | `set_ylim(None)` issue remains                                  | If `voltage_scale` is `None`, `ax.set_ylim(self.voltage_scale)` may be fragile. Only call it when not `None`. |
# | Scope stores arrays, not the signal object                      | This is okay, but a cleaner design might store `self.signal = signal` and derive displayed arrays from it.    |
#
# ### Most important remaining design improvement
#
# In `load_signal()`, consider storing the whole signal object:
#
# ```python
# self.signal = signal
# ```
#
# Then `current_signal`, `time`, and `fs` are display-derived state.
#
# Conceptually:
#
# ```text
# Signal owns:
#     tt, xt, fs
#
# Oscilloscope owns:
#     signal reference
#     voltage_scale
#     time_scale
#     displayed time
#     displayed samples
# ```
#
# Overall: **good revision**. This version now demonstrates the core OOP idea much better: the signal object owns the waveform, while the oscilloscope owns how that waveform is viewed.
#

# %%
