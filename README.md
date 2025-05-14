#  Modeling and Managing the Thermal Response of an Enclosed Chamber using Python and Runge-Kutta

This project simulates the **thermal response of an enclosed chamber** over time using the **Runge-Kutta 4th Order Method** in Python. It models how internal temperature changes in response to constant heat input, environmental heat loss, and system properties like surface area and air mass.

---

##  Project Objectives

- Understand and simulate heat transfer dynamics in a closed environment
- Apply the **Runge-Kutta method (RK4)** to solve the first-order ODE
- Visualize the temperature change over time using **Matplotlib**

---

## Core Concepts

- **ODE Solving** using RK4
- **Thermal systems modeling**: Incorporating real-world constants (heat input, ambient temperature, etc.)
- **Numerical Methods**: Approximating differential equations
- **Python Data Science Stack**: NumPy and Matplotlib

---

##  Sample Output

![Thermal Plot](thermal_plot.png)

- The orange curve shows how the **internal temperature rises** over time due to constant heat input.
- The blue dashed line shows the **ambient temperature** (25°C).
- The simulation models how the chamber approaches thermal equilibrium.

---

##  Code Overview

### Differential Equation Modeled:
\[
\frac{dT}{dt} = \frac{Q - hA(T - T_{\text{ambient}})}{m \cdot c}
\]

- `Q`: Heat input (W)
- `h`: Heat transfer coefficient (W/m²K)
- `A`: Surface area (m²)
- `m`: Mass of air (kg)
- `c`: Specific heat capacity (J/kgK)
- `T_ambient`: Ambient temperature (°C)

### Main Components

- `thermal_model()`: Defines the rate of change of temperature
- `Rungekutta4()`: Implements the RK4 method to approximate the temperature at each time step
- `matplotlib`: Used to visualize results

---

##  File Structure
thermal-response/
│
├── thermal_response.py # Python simulation script
├── thermal_plot.png # Sample output plot
└── README.md # Project documentation

---

##  How to Run

# Clone this repository
git clone (https://github.com/abdul-haleem21/Runge-Kutta-Using-python.git)
cd thermal-response

# Run the Python script
python thermal_response.py

Requirements

Python 3.x

NumPy

Matplotlib

You can install the required libraries with:

pip install numpy matplotlib
