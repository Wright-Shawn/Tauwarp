import numpy as np
from tauwarp import tau_poly

# Sketch: show how a τ warp would remap time stamps of “standard candles”
t = np.linspace(0, 1.0e17, 50)  # seconds
eps = 1e-18
tau = tau_poly(t, eps)
print("Mean fractional warp:", np.mean((tau - t)/t[1:]))
