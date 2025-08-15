import numpy as np
from tauwarp import tau_poly, tau_log

def test_tau_poly_zero():
    t = np.array([0., 1., 2.])
    assert np.allclose(tau_poly(t, 0.0), t)

def test_tau_log_monotonic():
    t = np.array([0.1, 1.0, 10.0])
    out = tau_log(t, 1e-3)
    assert np.all(np.diff(out) > 0)
