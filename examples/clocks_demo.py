import numpy as np
from tauwarp import tau_poly, phase_residual, fit_epsilon_grid

# Synthetic “frequency clock” residuals (radians) over 100 days
t = np.linspace(0, 100*86400.0, 2000)  # seconds
omega = 2*np.pi*1.0  # 1 Hz nominal
true_eps = 1e-18
y = phase_residual(t, true_eps, tau_poly, omega)

# Add noise to mimic measurement
rng = np.random.default_rng(42)
y_noisy = y + rng.normal(0, 1e-6, size=t.size)

eps_grid = np.linspace(-5e-18, 5e-18, 101)
best, chi2s = fit_epsilon_grid(phase_residual, t, y_noisy, tau_poly, eps_grid, omega=omega)
print("Recovered ε ~", best)
