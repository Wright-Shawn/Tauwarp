import numpy as np

def tau_poly(t, eps):
    """Model A: τ = t + ε t^2"""
    t = np.asarray(t, dtype=float)
    return t + eps * t**2

def tau_log(t, eps):
    """Model B: τ = t (1 + ε ln t), t>0"""
    t = np.asarray(t, dtype=float)
    if np.any(t <= 0):
        raise ValueError("tau_log requires t > 0.")
    return t * (1.0 + eps * np.log(t))
