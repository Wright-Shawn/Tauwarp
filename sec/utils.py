import numpy as np

def fit_epsilon_grid(make_residual, t, y_resid, model, eps_grid, **kwargs):
    """
    Brutal but informative grid search for ε:
    - make_residual: function(t, eps, model, **kwargs)->residual prediction
    - y_resid: observed residuals to match (same shape as t)
    Returns (eps_best, chi2_array)
    """
    chi2s = []
    for eps in eps_grid:
        pred = make_residual(t, eps, model, **kwargs)
        chi2 = np.sum((y_resid - pred)**2)
        chi2s.append(chi2)
    chi2s = np.asarray(chi2s)
    idx = int(np.argmin(chi2s))
    return eps_grid[idx], chi2s
