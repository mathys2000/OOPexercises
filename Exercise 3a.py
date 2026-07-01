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
# # Exercise 3a
#
# Phase 3 -- Multiple interacting objects
#
# Most real OOP begins here.
#
# Exercise 3: Communication chain
#
# Source, Encoder, Channel, Decoder, Receiver

# %%
import numpy as np


# %% [markdown]
# Create:
#
# ```python
# class Source:
# ```
#
# Internal state:
#
# ```python
# text
# LSBfirst
# ```
#
# Methods:
#
# ```python
# generate()
# ```
#

# %%
class Source:

    def __init__(self, text, LSBfirst=1):
        self.text = text
        self.LSBfirst = LSBfirst
        self.bits = None

    def generate(self):
        bitsperchar = 8
        textnum = np.array([ord(c) for c in self.text])  # convert ASCII to numeric
        if self.LSBfirst == 1:
            p2 = np.power(2.0, np.arange(0, -bitsperchar, -1))
        else:
            p2 = np.power(2.0, 1 + np.arange(-bitsperchar, 0))
        B = np.array(np.mod(np.array(np.floor(np.outer(textnum, p2)), int), 2), np.int8)
        self.bits = np.reshape(B, B.size)
        return self.bits
        


# %%
src = Source("Hi")
bits = src.generate()
print(bits)

# %%
