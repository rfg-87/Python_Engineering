# Ballistic Flight Simulator v1.0

A simple one-dimensional vertical-flight simulator written in Python to study numerical time integration with the **Explicit Euler method**.

The project propagates altitude and vertical velocity step by step under constant gravitational acceleration, compares the numerical solution with the analytical solution, and studies how the numerical error changes as the time step 'dt' is reduced.

## Objectives

This first version was developed as a learning project to practice:

- Translating differential equations into an algorithm.
- 'while' loops and stopping conditions.
- State propagation from step 'k' to step 'k + 1'.
- Fixed-step numerical integration.
- Explicit Eurler discretization.
- Analytical validation of a numerical model.
- Absolute/relative error analysis.
- Convergence with decreasing time step.

## Physical Model

The simulated motion is purely vertical and assumes constant gravitational acceleration, with no aerodynamic drag, thrust or mass variation.

The governing Ordinary Differential Equations (ODE) are:

$$
\frac{dh}{dt}=v
$$

$$
\frac{dv}{dt}=-g
$$

Where:

- $h$ is altitude in `[m]`;
- $v$ is vertical velocity in `[m/s]`;
- $g$ is gravitational acceleration in `[m/s^2]`.

The specific mechanical energy is also calculated during the simulation for inspection as a function of mass:

$$
E = gh + \frac{v^2}{2}
$$

with units of `[J/kg]`.

## Numerical Method

The equations are discretized using the **Explicit Euler Method**:

$$
h_{k+1}=h_k+v_k\Delta t
$$

$$
v_{k+1}=v_k-g\Delta t
$$

$$
t_{k+1}=t_k+\Delta t
$$

At every iteration, the complete new state is calculated first and then assigned to the current state. This avoids mixing values from different time steps.

The simulation continues while the altitude remains above or equal to ground level:

```python
while h >= 0:
    ...
```

## Inputs

The current version defines the simulation parameters directly in the Python script:

| Variable | Description | Units | Baseline value |
|---|---|---:|---:|
| `h0` | Initial altitude | m | 0 |
| `v0` | Initial vertical velocity | m/s | 50 |
| `t0` | Initial time | s | 0 |
| `g` | Gravitational acceleration | m/s² | 9.81 |
| `dt` | Integration time step | s | variable |

Input validation requires:

$$
h_0 \geq 0, \qquad v_0 > 0, \qquad g > 0, \qquad \Delta t > 0
$$

## Outputs

The simulator reports:

- numerical maximum altitude;
- numerical time of flight;
- numerical final velocity;
- iteration-by-iteration time, altitude, velocity, and specific mechanical energy;
- differences and percentage errors relative to the analytical solution.

## Analytical Validation

The numerical solution is compared against the closed-form solution for constant gravity.

Maximum altitude:

$$
h_{\max}=h_0+\frac{v_0^2}{2g}
$$

Time of flight until ground impact:

$$
t_f=\frac{v_0+\sqrt{v_0^2+2gh_0}}{g}
$$

Impact velocity:

$$
v_f=-\sqrt{v_0^2+2gh_0}
$$

For the baseline case (`h0 = 0 m`, `v0 = 50 m/s`, `g = 9.81 m/s²`), the analytical values are approximately:

| Quantity | Analytical value |
|---|---:|
| Maximum altitude | 127.421 m |
| Time of flight | 10.1937 s |
| Final velocity | -50.000 m/s |

## Time-Step Convergence Study

The simulator was executed with several values of `dt` to observe the convergence of the Explicit Euler solution.

| `dt` [s] | Euler max altitude [m] | Error in max altitude | Euler flight time [s] | Error in flight time |
|---:|---:|---:|---:|---:|
| 1.00 | 152.85 | 19.96% | 12.00 | 17.72% |
| 0.50 | 140.11 | 9.96% | 11.00 | 7.91% |
| 0.10 | 129.92 | 1.96% | 10.30 | 1.04% |
| 0.05 | 128.67 | 0.98% | 10.25 | 0.55% |
| 0.01 | 127.67 | 0.20% | 10.21 | 0.16% |

The results show that reducing `dt` drives the numerical solution toward the analytical solution. The maximum-altitude error decreases approximately in proportion to the time step, which is consistent with the first-order global accuracy of Explicit Euler.

The time-of-flight error is also affected by the simple impact detection used in this version: the simulation stops only after a full Euler step has crossed below `h = 0`, so the true impact occurs somewhere between the last two computed states.

## How to Run

No third-party Python packages are required. The program uses only the Python standard library.

From the project folder:

```bash
python ballistic_flight_simulator_v1.py
```

On some Windows installations you may instead use:

```bash
py ballistic_flight_simulator_v1.py
```

To run a different case, edit the input values near the beginning of the script, especially `h0`, `v0`, `g`, and `dt`.

## Project Structure

```text
ballistic_flight_simulator_v1/
├── ballistic_flight_simulator_v1.py
├── README.md
└── notes/
```

## Current Limitations

Version 1.0 intentionally keeps the model simple in order to focus on the numerical method. Current limitations include:

- one-dimensional vertical motion only;
- constant gravitational acceleration;
- no atmospheric model or aerodynamic drag;
- no thrust or variable mass;
- fixed integration step;
- Explicit Euler integration only;
- ground impact is not interpolated between time steps;
- trajectory data are printed to the terminal rather than stored in arrays/files;
- the code has not yet been refactored into reusable functions, modules, or classes.

Because Explicit Euler is not an energy-preserving integration scheme, the calculated specific mechanical energy may drift numerically. This becomes smaller as the time step is reduced.

## Possible Future Improvements

Future versions can progressively introduce:

1. interpolation of the exact ground-crossing event;
2. automated convergence studies and plots;
3. storage of trajectory data in arrays and output files;
4. refactoring into functions and reusable modules;
5. altitude-dependent gravity;
6. atmospheric density and aerodynamic drag;
7. thrust and variable rocket mass;
8. higher-order numerical integrators such as RK2 and RK4;
9. comparison with `scipy.integrate.solve_ivp`.

These additions can evolve the project from a simple ballistic model toward a more complete rocket-flight simulator.

## Learning Outcome

This project represents the transition from basic Python control flow to numerical engineering simulation:

```text
mathematical model
      ↓
differential equations
      ↓
discretization
      ↓
time-stepping algorithm
      ↓
numerical simulation
      ↓
analytical validation
      ↓
convergence study
```

The key idea is that the computer does not need a closed-form trajectory equation: it can propagate the physical state step by step from the governing differential equations.
