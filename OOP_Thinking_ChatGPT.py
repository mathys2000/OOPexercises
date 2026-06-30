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
# # OOP Thinking
#
# Prompt for ChatGPT-5.5 Plus:
#
# I'm new to object-oriented coding in python.
# I want to learn more using jupyter notebook examples and guidance on the underlying thinking and reasoning.
# I have a pretty good grasp of python in general but I'm not trained in object-oriented thinking.
# Set some goals and give me some meaningful exercises.
#

# %% [markdown]
# You already have a strong advantage: you know Python and you seem comfortable with technical subjects (DSP, decoding algorithms, embedded systems, EE teaching). The gap is probably **not syntax** — it is learning to think in terms of:
#
# > *What objects exist? What state do they own? What behavior belongs with that state? What responsibilities should be grouped together?*
#
# Most people learn OOP backwards by memorizing `class`, `__init__`, inheritance, etc. I’d suggest learning it in layers.
#
# ## Phase 1 — Learn object thinking (Week 1)
#
# ### Goal 1: Stop thinking “functions first”
#
# Instead of:
#
# ```python
# filter_signal(x)
# compute_fft(x)
# plot_signal(x)
# ```
#
# Ask:
#
# ```python
# sig = Signal(x)
#
# sig.filter()
# sig.fft()
# sig.plot()
# ```
#
# Question:
#
# **What owns the data?**
#
# The answer often becomes the object.
#
# ---
#
# ### Exercise 1: Build a `Signal` object
#
# Notebook: `01_signal_class.ipynb`
#
# Start with:
#
# ```python
# import numpy as np
# import matplotlib.pyplot as plt
#
# class Signal:
#
#     def __init__(self, samples, fs):
#         self.samples = np.array(samples)
#         self.fs = fs
#
#     def duration(self):
#         return len(self.samples) / self.fs
#
#     def energy(self):
#         return np.sum(self.samples**2)
#
#     def plot(self):
#
#         t = np.arange(len(self.samples))/self.fs
#
#         plt.plot(t, self.samples)
#         plt.xlabel("Time")
#         plt.ylabel("Amplitude")
#         plt.show()
# ```
#
# Try:
#
# ```python
# x = Signal(
#     samples=np.sin(np.linspace(0,10,200)),
#     fs=100
# )
#
# print(x.duration())
# print(x.energy())
#
# x.plot()
# ```
#
# ### Thinking exercise
#
# Ask:
#
# * Why is `fs` stored?
# * Why is `energy()` inside the object?
# * Should plotting belong here?
# * What should remain external?
#
# Write answers in notebook markdown cells.
#
# ---
#
# ## Phase 2 — State and behavior (Week 2)
#
# Objects exist because **state persists**.
#
# ### Exercise 2: Oscilloscope simulator
#
# Create:
#
# ```python
# class Oscilloscope:
# ```
#
# Internal state:
#
# ```python
# sample_rate
# voltage_scale
# time_scale
# current_signal
# ```
#
# Methods:
#
# ```python
# load_signal()
# autoscale()
# measure_rms()
# display()
# ```
#
# Example:
#
# ```python
# scope = Oscilloscope()
#
# scope.load_signal(sig)
#
# scope.autoscale()
#
# scope.display()
# ```
#
# Notebook questions:
#
# 1. Which variables belong to object state?
# 2. Which should be method arguments?
# 3. What happens if two scopes observe different signals?
#
# ---
#
# ## Phase 3 — Multiple interacting objects
#
# Most real OOP begins here.
#
# ### Exercise 3: Communication chain
#
# Build:
#
# ```python
# Source
# Encoder
# Channel
# Decoder
# Receiver
# ```
#
# Flow:
#
# ```python
# src = Source()
#
# enc = Encoder()
#
# ch = Channel()
#
# dec = Decoder()
#
# rx = Receiver()
#
# bits = src.generate()
#
# coded = enc.encode(bits)
#
# noisy = ch.transmit(coded)
#
# decoded = dec.decode(noisy)
#
# rx.evaluate(bits, decoded)
# ```
#
# This mirrors systems work and DSP pipelines.
#
# Ask:
#
# * Which object owns noise power?
# * Should BER live in Receiver?
# * Should channel know modulation?
#
# ---
#
# ## Phase 4 — Encapsulation and hidden internals
#
# Most beginners expose everything.
#
# Bad:
#
# ```python
# sig.samples = []
# sig.fs = -10
# ```
#
# Better:
#
# ```python
# class Signal:
#
#     def __init__(self,samples,fs):
#
#         self._samples = samples
#         self._fs = fs
#
#     @property
#     def fs(self):
#         return self._fs
# ```
#
# Exercise:
#
# Prevent illegal sample rate:
#
# ```python
# sig.fs = -5
# ```
#
# Raise:
#
# ```python
# ValueError
# ```
#
# ---
#
# ## Phase 5 — Inheritance (later, not first)
#
# Many tutorials start here.
#
# Do **not**.
#
# Learn composition first.
#
# Instead of:
#
# ```python
# class BPSKSignal(Signal)
# class QPSKSignal(Signal)
# ```
#
# Try:
#
# ```python
# class Modulator:
#
#     def __init__(self, scheme):
#         self.scheme = scheme
# ```
#
# Inheritance only when:
#
# > “A thing truly IS another thing”
#
# Example:
#
# ```python
# Signal
#     ├── AnalogSignal
#     └── DigitalSignal
# ```
#
# ---
#
# ## Phase 6 — Final project (important)
#
# Build a mini communications simulator:
#
# Classes:
#
# ```python
# BitSource
# ConvolutionalEncoder
# BPSKModulator
# AWGNChannel
# ViterbiDecoder
# BERCounter
# Simulation
# ```
#
# Run:
#
# ```python
# sim = Simulation()
#
# sim.run()
#
# sim.plot_results()
# ```
#
# Given your previous work with Viterbi decoding, this will feel natural and show where OOP becomes useful.
#
# ---
#
# # Suggested learning milestones
#
# | Stage | Concept             | Deliverable                             |
# | ----- | ------------------- | --------------------------------------- |
# | 1     | Objects and state   | `Signal` class                          |
# | 2     | State ownership     | `Oscilloscope`                          |
# | 3     | Collaboration       | Communication chain                     |
# | 4     | Encapsulation       | Protected members + validation          |
# | 5     | Composition         | Modulator framework                     |
# | 6     | Larger architecture | Full simulator                          |
# | 7     | Advanced            | Abstract classes, dataclasses, patterns |
#
# ---
#
# ## Jupyter habit I strongly recommend
#
# For every notebook:
#
# ### Cell 1
#
# ```python
# # OBJECT MAP
#
# Signal
#     state:
#         samples
#         fs
#
#     behavior:
#         energy()
#         plot()
#         fft()
# ```
#
# ### Cell 2
#
# Write:
#
# > What owns the data?
#
# ### Cell 3
#
# Write:
#
# > Which object is responsible?
#
# This trains OOP thinking much faster than coding alone.
#
# ---
#
# ## Stretch exercise
#
# Take an existing procedural script you already have (FFT demo, filter analysis, Viterbi example, Arduino serial monitor, BER simulation).
#
# Refactor:
#
# Procedural:
#
# ```python
# generate()
# encode()
# channel()
# decode()
# measure()
# ```
#
# OOP:
#
# ```python
# Simulation
# Source
# Encoder
# Channel
# Decoder
# Metrics
# ```
#
# Then answer:
#
# 1. What state moved into objects?
# 2. What became easier?
# 3. What became harder?
# 4. Did coupling improve?
#
# That reflection is where object-oriented intuition develops.
#
# If you want, next I can lay out a **10-notebook sequence with increasing difficulty and complete notebook templates**.
#
# [1]: https://chatgpt.com/c/68926d01-4fb0-8326-a0a5-81de854fe901 "Create lecture notes"
# [2]: https://chatgpt.com/c/6948a95c-1488-8330-9720-a27515593484 "Linear Systems lesson plan"
# [3]: https://chatgpt.com/c/68a613f6-fb34-8329-87d4-9018a484b008 "Viterbi decoder Python"
# [4]: https://chatgpt.com/c/6976ac79-2b5c-8333-b7b0-67128f7377a8 "Exam for Signals & Systems"
# [5]: https://chatgpt.com/c/66fae79f-c2c8-800f-abdd-f4eb7d4602e6 "Frequency Response of Systems"
# [6]: https://chatgpt.com/c/69add106-4eb0-8333-9b54-0188acbbed17 "Lab Report Review"
# [7]: https://chatgpt.com/c/66f1ef1e-1604-800f-b742-005a7aa39dd2 "DSP Filter Project Overview"
# [8]: https://chatgpt.com/c/69cd8ba5-ea4c-83e8-b137-17d61229204f "Paper Review Summary"
# [9]: https://chatgpt.com/c/69ed859a-efd0-83e8-806d-aef674bb7071 "Lab Report Review"
# [10]: https://chatgpt.com/c/69efcabb-dbcc-83e8-8d33-25b07a6d9c44 "Arduino Nano Every Interrupts"
#
#

# %%
