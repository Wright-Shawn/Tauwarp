import numpy as np
from tauwarp import tau_log, phase_residual

# Toy MSP: 1000 Hz spin, 10 years sampled monthly
t = np.linspace(1.0, 10*365.25*86400.0, 120)  # start at t>0 for log
omega = 2*np.pi*1000.0
eps = 5e-19
res = phase_residual(t, eps, tau_log, omega)
print("RMS phase warp (rad):", np.sqrt(np.mean(res**2)))
