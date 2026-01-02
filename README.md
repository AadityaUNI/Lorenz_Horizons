# Lorenz Horizon

## About the Project
This is a visual Lorenz Attractor Model Simulator which offers the user full control over the parameters - Sigma, Beta & Rho, along with initial positions.

The App allows simulating two lorenz models in a 3d interactive plotly graph:
<img width="943" height="891" alt="image" src="https://github.com/user-attachments/assets/2769140f-ea9c-48d7-a92a-3833ac8ad8ec" />


And another feature the user can explore is the **Predictability Horizon**:
<img width="948" height="921" alt="image" src="https://github.com/user-attachments/assets/c3d497d9-fa95-4338-8fa0-6681a83c35c5" />


This is defined (by me) as the earliest time at which the correlation between two Lorenz trajectories falls below a fixed threshold and remains below that threshold for a sustained duration, indicating 
a persistent loss of reliable predictability rather than a transient fluctuation.

For the example shown above, the horizon plot demonstrating the threshold (horizontal -- line) and the time (vertical red line) at which the horizon is significantly crossed:

This project was purely motivated by personal curiosity within lorenz attractor systems and to understand (and tinker with) the different values of the constants pertaining to different system behaviors along 
with an added research feature as my own twist.

## Installation

### Requirements
- Python 3.9+ (recommended)

### Install dependencies
```bash
pip install -r requirements.txt
```

## Running the app
```bash
python app.py
```

## Presets (pre-defined values)
The simulator includes a small set of pre-defined parameter presets (Sigma, Beta, Rho) used to demonstrate different Lorenz attractor behaviors.

These are defined in `Simulator.py` as `PreDefMap` and labeled via `BehaviorMap`:

- **1. Atmospheric Heat Convections (Chaotic)**
  - Constants: `sigma=10`, `beta=8/3`, `rho=28`
  - Label: "Chaotic Convections"

- **2. The Torus Knot (Periodic)**
  - Constants: `sigma=10`, `beta=8/3`, `rho=99.65`
  - Label: "Torus Knot (Periodic)"

- **3. The Stable Point (Stabilizes)**
  - Constants: `sigma=10`, `beta=8/3`, `rho=15`
  - Label: "Stable Point"

- **4. Intermittency (Chaotic Bursts)**
  - Constants: `sigma=10`, `beta=8/3`, `rho=166.072`
  - Label: "Chaotic Bursts"

> Note: all presets currently use the same default initial state `x=y=z=1` unless you choose custom initial values.
