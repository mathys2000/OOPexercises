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
# # OOP Notebooks
#
# ChatGPT-5.5 Plus Prompt:
#
# Yes, lay out that 10 notebook sequence
#

# %% [markdown]
# I’d structure it as a mini course where each notebook introduces **one new OOP idea** and ends with a meaningful engineering-style exercise. Since you already know Python, I’d avoid toy examples like “Dog” and “Car” and stay close to signals, systems, instrumentation, and simulation.
#
# # Notebook 1 — Objects as State Containers
#
# **File:** `01_objects_and_state.ipynb`
#
# ### Main idea
#
# Objects store **state + behavior**.
#
# Build:
#
# ```python
# Signal
# ```
#
# State:
#
# ```python
# samples
# fs
# name
# ```
#
# Methods:
#
# ```python
# duration()
# energy()
# mean()
# plot()
# ```
#
# Exercises:
#
# 1. Add RMS calculation
# 2. Add peak detection
# 3. Add signal normalization
# 4. Compare two signals
#
# Reflection:
#
# > Which variables belong permanently to the signal?
#
# Deliverable:
#
# ```python
# sig = Signal(x,1000)
#
# sig.energy()
#
# sig.plot()
# ```
#
# ---
#
# # Notebook 2 — Responsibility and Encapsulation
#
# **File:** `02_encapsulation.ipynb`
#
# ### Main idea
#
# Protect object integrity.
#
# Build:
#
# ```python
# class Signal:
# ```
#
# Add validation:
#
# ```python
# fs > 0
# samples not empty
# ```
#
# Introduce:
#
# ```python
# @property
# setter
# private variables
# ```
#
# Example:
#
# ```python
# sig.fs = -100
# ```
#
# Should produce:
#
# ```python
# ValueError
# ```
#
# Exercises:
#
# 1. Prevent invalid sample rate
# 2. Prevent NaNs
# 3. Add readonly duration property
# 4. Log state changes
#
# Reflection:
#
# > What should users be allowed to change?
#
# ---
#
# # Notebook 3 — Objects Interacting
#
# **File:** `03_object_collaboration.ipynb`
#
# Create chain:
#
# ```python
# Source
# Encoder
# Channel
# Receiver
# ```
#
# Pipeline:
#
# ```python
# src.generate()
#
# enc.encode()
#
# ch.transmit()
#
# rx.detect()
# ```
#
# Exercises:
#
# Build:
#
# * Binary source
# * Noise channel
# * Error counter
#
# Questions:
#
# * Who owns BER?
# * Who owns noise variance?
# * Should source know channel?
#
# Goal:
#
# Learn **separation of responsibility**.
#
# ---
#
# # Notebook 4 — Composition vs Inheritance
#
# **File:** `04_composition_vs_inheritance.ipynb`
#
# Start wrong:
#
# ```python
# Signal
#     BPSKSignal
#     QPSKSignal
#     OFDMSignal
# ```
#
# Then redesign:
#
# ```python
# Signal
#
# Modulator
#
# Channel
# ```
#
# Composition:
#
# ```python
# sig = Signal(bits)
#
# mod = Modulator("BPSK")
#
# wave = mod.modulate(sig)
# ```
#
# Exercises:
#
# 1. Compare both architectures
# 2. Add QPSK
# 3. Add ASK
# 4. Measure complexity
#
# Reflection:
#
# > When is “is-a” wrong?
#
# ---
#
# # Notebook 5 — Simulation Framework
#
# **File:** `05_simulation_engine.ipynb`
#
# Create:
#
# ```python
# Simulation
# ```
#
# Contains:
#
# ```python
# source
# encoder
# channel
# receiver
# metrics
# ```
#
# Run:
#
# ```python
# sim.run()
# ```
#
# Add:
#
# ```python
# reset()
# step()
# summary()
# ```
#
# Exercises:
#
# Run BER experiments.
#
# Store:
#
# ```python
# EbN0
# BER
# iterations
# ```
#
# Goal:
#
# Learn orchestration objects.
#
# ---
#
# # Notebook 6 — Polymorphism
#
# **File:** `06_polymorphism.ipynb`
#
# Create interface style behavior:
#
# ```python
# Channel
# ```
#
# Derived:
#
# ```python
# AWGNChannel
#
# FadingChannel
#
# InterferenceChannel
# ```
#
# Same call:
#
# ```python
# channel.transmit(x)
# ```
#
# Swap:
#
# ```python
# sim.channel = AWGNChannel()
#
# sim.channel = FadingChannel()
# ```
#
# Exercises:
#
# 1. Add impulsive noise
# 2. Add burst errors
# 3. Compare outputs
#
# Reflection:
#
# > Why does identical API matter?
#
# ---
#
# # Notebook 7 — Instrument Modeling
#
# **File:** `07_virtual_instruments.ipynb`
#
# Build:
#
# ```python
# Oscilloscope
# SpectrumAnalyzer
# SignalGenerator
# ```
#
# Interactions:
#
# ```python
# gen.generate()
#
# scope.measure()
#
# spec.compute_fft()
# ```
#
# Exercises:
#
# Add:
#
# * trigger level
# * autoscale
# * peak hold
# * bandwidth limits
#
# Goal:
#
# Objects with persistent state.
#
# ---
#
# # Notebook 8 — Dataclasses and Cleaner Design
#
# **File:** `08_dataclasses.ipynb`
#
# Introduce:
#
# ```python
# from dataclasses import dataclass
# ```
#
# Example:
#
# ```python
# @dataclass
# class ChannelConfig:
#
#     snr: float
#
#     fading: bool
#
#     seed: int
# ```
#
# Exercises:
#
# Convert:
#
# ```python
# SignalConfig
#
# ReceiverConfig
#
# SimulationConfig
# ```
#
# Reflection:
#
# > When should classes contain data only?
#
# ---
#
# # Notebook 9 — Design Patterns (Practical)
#
# **File:** `09_patterns.ipynb`
#
# Pattern 1:
#
# Factory
#
# ```python
# factory.make_channel(
#     "awgn"
# )
# ```
#
# Pattern 2:
#
# Strategy
#
# ```python
# decoder = Viterbi()
#
# decoder = MLDecoder()
# ```
#
# Pattern 3:
#
# Observer
#
# ```python
# scope.subscribe(signal)
# ```
#
# Exercises:
#
# Build channel factory.
#
# Add decoder switching.
#
# Goal:
#
# See reusable architectures.
#
# ---
#
# # Notebook 10 — Capstone Project
#
# **File:** `10_comm_system_project.ipynb`
#
# Build complete simulator:
#
# ```python
# BitSource
#
# ConvolutionalEncoder
#
# Interleaver
#
# BPSKModulator
#
# AWGNChannel
#
# ViterbiDecoder
#
# BERCounter
#
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
# sim.plot_ber()
# ```
#
# Add:
#
# ```python
# save_results()
#
# export_csv()
#
# parameter_sweep()
# ```
#
# Final challenge:
#
# Create:
#
# ```python
# MonteCarloRunner
# ```
#
# for:
#
# ```python
# EbN0 = np.arange(
#     0,
#     10,
#     1
# )
# ```
#
# Generate BER curves.
#
# ---
#
# # Recommended notebook workflow
#
# Every notebook should start with:
#
# ```markdown
# # Object map
#
# Signal
#
# State:
# - samples
# - fs
# - name
#
# Behavior:
# - energy()
# - plot()
# - fft()
# ```
#
# Then:
#
# ```markdown
# Responsibilities:
#
# Signal owns:
# ✓ samples
# ✓ sampling rate
#
# Signal does NOT own:
# ✗ channel noise
# ✗ BER
# ✗ decoder state
# ```
#
# Then:
#
# ```markdown
# Design questions
#
# 1. What persists?
#
# 2. Who owns it?
#
# 3. What should remain hidden?
#
# 4. Which objects collaborate?
# ```
#
# ---
#
# # Difficulty progression
#
# | Notebook | Topic             | Difficulty  |
# | -------- | ----------------- | ----------- |
# | 1        | Objects/state     | Easy        |
# | 2        | Encapsulation     | Easy        |
# | 3        | Collaboration     | Medium      |
# | 4        | Composition       | Medium      |
# | 5        | Framework design  | Medium      |
# | 6        | Polymorphism      | Medium–Hard |
# | 7        | Instrument models | Hard        |
# | 8        | Dataclasses       | Medium      |
# | 9        | Patterns          | Hard        |
# | 10       | Full simulator    | Advanced    |
#
# If you complete all ten, you will move from **“I know Python syntax”** to **“I can architect medium-size OOP systems.”**
#
#

# %%
