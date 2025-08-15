import numpy as np

def phase_residual(t, eps, model, omega):
    """
    Residual phase under a warp for a pure oscillator with angular freq omega.
    Reference phase: φ_ref(t) = omega * t
    Warped phase:    φ_tau(t) = omega * τ(t)
    Residual: Δφ = φ_tau - φ_ref = omega * (τ(t) - t)
    """
    t = np.asarray(t, dtype=float)
    tau = model(t, eps)
    return omega * (tau - t)

def exp_decay_residual(t, eps, model, lam):
    """
    Residual for exponential decay N(t)=N0 exp(-λ τ(t)) vs exp(-λ t).
    Return fractional deviation R = N_tau/N_lin - 1 = exp(-λ(τ - t)) - 1
    """
    t = np.asarray(t, dtype=float)
    tau = model(t, eps)
    return np.exp(-lam * (tau - t)) - 1.0
