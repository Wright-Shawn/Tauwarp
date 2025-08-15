# Tauwarp

Tauwarp — n. A research framework for re-parameterizing clock time t into a hypothesized “true time” variable \tau using non-linear mappings, and testing the resulting predictions against precision measurements from laboratory, astrophysical, and cosmological systems.

Testing the limits of linear time — Tools and workflows for probing non-linear time hypotheses using data from atomic clocks, pulsars, and cosmology.

⸻

## Overview

This repository implements the Non-Linear Time Hypothesis, which proposes that the true physical time variable \tau may be a non-linear function of laboratory time t:

\tau = f(t) \neq at + b

If true, this would leave a subtle but universal fingerprint across every process with a predictable time law — from the ticking of atomic clocks, to pulsar rotations, to the expansion history of the universe.

## Tauwarp provides:

 •	Functions to re-parameterize time series (t \to \tau) under simple test forms like \tau = t + \varepsilon t^2.

 •	Residual-generation tools to see how these warps affect different datasets.

 •	Bayesian fitting workflows for cross-domain constraints on the warp parameter ε.

⸻

## Why it matters

Time is treated as linear in all mainstream physics, but this assumption has never been directly tested across the widest possible range of scales.

Tauwarp enables a unified analysis using:

 •	Laboratory clocks — long-term optical and microwave comparisons.

 •	Astrophysical timers — millisecond pulsars, gravitational-wave chirps, strong-lens delays.

 •	Cosmological baselines — supernovae, BAO, and CMB acoustic features.

By applying the same model across radically different domains, we can either:

 •	Set the tightest cross-domain bounds yet on non-linear time.

 •	Or detect a consistent deviation worth deeper investigation.

## Data

This project can operate on **synthetic** data or public datasets.

- Place tiny synthetic CSVs in `data/samples/` (ignored by git).
- For public datasets, link to the source and keep only scripts that download/process them.

## 📄 Citation

If you use **tauwarp** in your work, please cite it as follows:

**APA Style**  
Wright, S. C. (2025). *tauwarp: Non-linear Time Re-parameterization Toolkit* (Version 0.0.1) [Computer software]. GitHub. https://github.com/Wright-Shawn/tauwarp

**BibTeX**  
```bibtex
@software{wright2025tauwarp,
  author = {Wright, Shawn C.},
  title = {tauwarp: Non-linear Time Re-parameterization Toolkit},
  url = {https://github.com/Wright-Shawn/tauwarp},
  version = {0.0.1},
  date = {2025-08-15},
  license = {Apache-2.0}
}
