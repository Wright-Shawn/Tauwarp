import numpy as np
from tauwarp import tau_poly, warp_time, unwarp_time

def test_unwarp_roundtrip():
    t = np.linspace(0.0, 1000.0, 101)
    eps = 1e-6
    tau = warp_time(t, tau_poly, eps)
    t_back = unwarp_time(tau, tau_poly, eps)
    assert np.allclose(t, t_back, rtol=0, atol=1e-6)
