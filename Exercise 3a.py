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
rng = np.random.default_rng()


# %% [markdown]
# ## Source Class
#
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
# set_text()
# set_LSBfirst()
# generate()
# ```
#

# %%
class Source:

    def __init__(self, text, LSBfirst=1):
        if len(text) < 1:
            raise ValueError("text must have length > 1")
        self.text = text
        self.LSBfirst = LSBfirst
        
    def set_text(self, text):
        self.text = text

    def set_LSBfirst(self, LSBfirst):
        self.LSBfirst = LSBfirst
    
    def generate(self):
        bitsperchar = 8
        textnum = np.array([ord(c) for c in self.text])  # convert ASCII to numeric
        if self.LSBfirst == 1:
            p2 = np.power(2.0, np.arange(0, -bitsperchar, -1))
        else:
            p2 = np.power(2.0, 1 + np.arange(-bitsperchar, 0))
        B = np.array(np.mod(np.array(np.floor(np.outer(textnum, p2)), int), 2), np.int8)
        bits = np.reshape(B, B.size)
        return bits
        


# %%
src = Source("Hi")
bits = src.generate()
print(src.LSBfirst)
print(bits)

# %%
src.set_LSBfirst(0)
bits = src.generate()
print(src.LSBfirst)
print(bits)


# %%
#src.set_text("Bye!")
#src.set_LSBfirst(1)
#bits = src.generate()
#print(src.LSBfirst)
#print(bits)

# %% [markdown]
# ## Receiver Class
#
# Create:
#
# ```python
# class Receiver:
# ```
#
# Internal state:
#
# ```python
# decoded
# LSBfirst
# ```
#
# Methods:
#
# ```python
# BER()
# received_text()
# ```
#

# %%
class Receiver:

    def __init__(self, decoded, LSBfirst=1):
        self.decoded = decoded
        self.LSBfirst = LSBfirst
        
    def BER(self, bits):    # bit error rate (fraction of incorrectly decoded bits)
        L = min(len(bits), len(self.decoded))
        BER = np.where(bits!=self.decoded)[0].size/L
        return BER

    def received_text(self):
        bitsperchar = 8
        dnb = self.decoded[0:bitsperchar*int(len(self.decoded)/bitsperchar)]
                         # make multiple of bitsperchar long
        B = np.array(np.reshape(dnb, (int(len(dnb)/bitsperchar), bitsperchar)), int)
        if self.LSBfirst == 1:
            p2 = np.power(2, np.arange(0, bitsperchar))
        else:
            p2 = np.power(2, np.arange(bitsperchar, 0, -1) - 1)
        textnum = np.array(np.dot(B, p2))
        textrx = ''.join(chr(n) for n in textnum)
        return textrx



# %%
decoded = src.generate()
decoded[3] = np.mod(1+decoded[3],2) 
rx = Receiver(decoded, src.LSBfirst)

# %%
print(rx.BER(src.generate()))
print(rx.received_text())


# %% [markdown]
# ## Channel Class
#
# Create:
#
# ```python
# class Channel:
# ```
#
# Internal state:
#
# ```python
# PbE    # Probability of bit error
# ```
#
# Methods:
#
# ```python
# transmit()
# get_PbE()
# set_PbE()
# ```
#

# %%
class Channel:

    def __init__(self, PbE):
        if (PbE < 0) or (PbE > 1):
            raise ValueError("PbE must be in range 0...1.0")
        self.PbE = PbE

    def get_PbE(self):
        return self.PbE

    def set_PbE(self, PbE):
        if (PbE < 0) or (PbE > 1):
            raise ValueError("PbE must be in range 0...1.0")
        self.PbE = PbE
    
    def transmit(self, binary_in):
        L = len(binary_in)
        ix = np.where(rng.random(L) <= self.PbE)
        out = binary_in.copy()
        out[ix] = np.mod(out[ix] + 1, 2)   # flip error bits
        return out



# %%
src = Source("The quick brown fox jumps over the lazy dog 0123456789")
ch = Channel(0.01)
decoded = ch.transmit(src.generate())
rx = Receiver(decoded, src.LSBfirst)
print(f'BER: {rx.BER(src.generate())}')
print(rx.received_text())


# %% [markdown]
# ## Encoder Class
#
# Create:
#
# ```python
# class Encoder:
# ```
#
# Internal state:
#
# ```python
# G    # Encoder matrix
# ```
#
# Methods:
#
# ```python
# encode()
# ```
#

# %%
class Encoder:

    def __init__(self, G):
        self.G = np.array(G, int)
        self.k, self.n = np.shape(G)

    def encode(self, src):
        N = int(np.ceil(len(src)/self.k))
        src_pad = np.zeros(N*self.k, int)
        src_pad[:len(src)] = src
        u = np.reshape(src_pad, (-1, self.k))   # split src string into blocks of length k
        B = np.mod(u@self.G, 2)
        return np.reshape(B, (1, -1))



# %%
src2 = Source('Hi!')
G = [[1,0,0,0,1,1,1],[0,1,0,0,1,1,0],[0,0,1,0,1,0,1],[0,0,0,1,0,1,1]]
enc = Encoder(G)
coded = enc.encode(src2.generate())
print(coded)


# %% [markdown]
# ## Decoder Class
#
# Create:
#
# ```python
# class Decoder:
# ```
#
# Internal state:
#
# ```python
# H    # Parity check matrix
# ```
#
# Methods:
#
# ```python
# decode()
# syndrome()
# ```
#

# %%
