import numpy as np

def warp_time(t, model, eps):
    """Apply t→τ warp using a model function(t, eps)."""
    return model(t, eps)

def unwarp_time(tau, model, eps, t0=None, maxiter=50, tol=1e-12):
    """
    Invert τ = f(t) via Newton iterations.
    Assumes small |eps| and monotonic f.
    """
    tau = np.asarray(tau, dtype=float)
    # Initial guess
    if t0 is None:
        t = tau.copy()
    else:
        t = np.full_like(tau, t0, dtype=float)

    # Numerical derivative via central diff
    def f(x): return model(x, eps)

    for _ in range(maxiter):
        fx = f(t) - tau
        # Jacobian via finite diff
        h = np.maximum(1e-8, 1e-8 * np.abs(t))
        df = (f(t + h) - f(t - h)) / (2*h)
        step = fx / df
        t_next = t - step
        if np.max(np.abs(step)) < tol:
            return t_next
        t = t_next
    raise RuntimeError("unwarp_time did not converge")
