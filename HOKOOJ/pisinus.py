import numpy as np
import time as t

def pipisinus(freq, time):
    return (np.sin(2 * np.pi * freq * time) + 1) / 2

def wait(samp_freq):
    t.sleep(1.0/ samp_freq)
