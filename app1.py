# Mini Project Title: Modeling and Managing the Thermal Response of an Enclosed Chamber using Python and Runge-Kutta
# Description: This script simulates the thermal response of an enclosed chamber using the Runge-Kutta method.
# import necessary libraries
import numpy as np # This library is used for numerical operations and array manipulations.
import matplotlib.pyplot as plt # This library is used for plotting graphs and visualizing data.
# this is a simple simulation of the thermal response of an enclosed chamber using the Runge-Kutta method.
# The simulation models the temperature change over time based on heat input, heat transfer coefficient, surface area, mass of air, specific heat capacity, and ambient temperature.
# The Runge-Kutta method is a numerical technique used to solve ordinary differential equations (ODEs).

# Constants
# These constants represent the parameters of the thermal system being modeled.
# Q IS THE CONSTANT HEAT ENERGY OR INPUT BEING ADDED
# h  HOW EASILY HEAT IS TRANSFERRED TO THE ENVIRONMENT OR IS THE HEAT TRANSFER COEFFICIENT
# A IS HOW MUCH SURFACE IS EXPOSED FOR HEAT TO ESCAPE OR IS THE SURFACE AREA OF THE CHAMBER
# M IS HOW MUCH AIR IS INSIDE THE CHAMBER(AFFECTS HOW FAST IT HEATS UP)
# C IS HOW MUCH ENERGY IS NEEDED TO CHANGE THE AIR'S TEMPERATURE OR IS HOW MUCH ENERGY IT TAKES TO RAISE THE TEMPERATURE OF THE AIR INSIDE THE CHAMBER
# T_AMBIENT IS OUTSIDE TEMPERATURE, USED TO COMPUTE HEAT LOSS

Q = 50  # Heat input (W)
h = 100  # Heat transfer coefficient (W/m^2K)
A = 0.2  # Surface area (m^2)
m = 0.5 # Mass of air (kg)
c = 600  # Specific heat capacity of air (J/kgK)
T_ambient = 25 # Ambient temmperature (k)

# Differential equation: dT/dt = (Q - hA(T - T_ambient)) / (m * c)
def thermal_model(t, T):
    return (Q - h *A * (T - T_ambient)) / (m * c) # This represents the First oder ODE for the thermal system which is "dT/dt = (Q - hA(T - T_ambient)) / (m * c)"
# t AND T ARE INPUTS TO THE FUNCTION
# t IS TIME (NOT USED DIRECTLY BUT REQUIRED FOR RUNGE-KUTTA 4TH ORDER METHOD FORMAT)
# T IS CURRENT INTERNAL TEMPERATURE
# OUTPUT IS THE RATE OF CHANGE OF TEMPERATURE AT THAT MOMENT
# This function calculates the rate of change of temperature (dT/dt) based on the heat input (Q), heat transfer coefficient (h), surface area (A), mass of air (m),



# Runge-Kutta 4th order method Function
def Rungekutta4(f, T0, t0, tf, dt):
    # This function implements the Runge-Kutta 4th order method to solve the ODE.
    # f is the function representing the ODE
    # T0 is the initial temperature
    # t0 is the initial time
    # tf is the final time
    # dt is the time step
    # The function returns the time and temperature arrays after solving the ODE using the Runge-Kutta method.

    # Initialize variables
    N = int((tf - t0) / dt)  # Number of steps (N) needed between (t0) and (tf) based on (dt).
    T = np.zeros(N + 1)  # Initialize the array to store temperature values
    t = np.linspace(t0, tf, N + 1)  # Create an array of time values from t0 to tf
    T[0] = T0  # Set the initial temperature
# N is the number of steps, T is the array to store temperature values, t is the array of time values, and T[0] is the initial temperature.
    # The Runge-Kutta method is a numerical technique used to solve ordinary differential equations (ODEs).
    # It approximates the solution by calculating slopes at different points and combining them to get a more accurate result.
    # In this case, it is used to model the thermal response of an enclosed chamber over time.


# Runge-Kutta 4th order Loop

    for i in range(N):
        # This loop iterates through each time step to calculate the temperature using the Runge-Kutta method.
        # The loop runs N times, where N is the number of steps calculated earlier.
        # In each iteration, it calculates the slopes (k1, k2, k3, k4) based on the current temperature and time.
        # The slopes are then combined to update the temperature for the next time step.
        # The slopes (k1, k2, k3, k4) are calculated using the thermal_model function.
        # The first slope (k1) is calculated using the current temperature and time.
        # The second slope (k2) is calculated using the time and temperature at the midpoint of the interval.
        # The third slope (k3) is calculated using the time and temperature at the midpoint of the interval.    
        # The fourth slope (k4) is calculated using the time and temperature at the end of the interval.
        # The temperature for the next time step (T[i + 1]) is then calculated using the slopes.
        # The slopes are combined using the formula: T[i + 1] = T[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
        # This formula is derived from the Runge-Kutta method and provides a more accurate estimate of the temperature at the next time step.
        k1 = dt* f(t[i], T[i]) # Calculate the first slope
        k2 = dt* f(t[i] + dt/2, T[i] + k1/2) # Calculate the second slope
        k3 = dt* f(t[i] + dt/2, T[i] + k2/2) # Calculate the third slope
        k4 = dt* f(t[i] + dt, T[i] + k3) # Calculate the fourth slope
        T[i + 1] = T[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
 # K1 IS THE INITIAL SLOPE
 # K2 IS THE SLOPE AT THE MIDPOINT OF THE INTERVAL USING K1
 # K3 IS THE SLOPE AT THE MIDPOINT OF THE INTERVAL USING K2      
 # K4 IS THE SLOPE AT THE END OF THE INTERVAL USING K3
        return t, T # Return the time and temperature arrays
# Initial Setup this sets up the simulation for 10 minutes(600 seconds), starting at ambient temmperature.
T0 = 50  # Initial temperature (C)  
t0 = 0  # Initial time (s)
tf = 100  # Final time (s)
dt = 1  # Time step (s)

# Run the simulation
time, temperature = Rungekutta4(thermal_model, T0, t0, tf, dt) # This calls or Runs Runge-kutta 4th order function with model and parameters to generate results.


# Plotting the results
plt.figure(figsize=(10,5)) # Create a figure for plotting
plt.plot(time, temperature, label='Internal Temperature (°C)', color='orange') # Plot the temperature over time
plt.axhline(y=T_ambient, color='blue', linestyle='--', label='Ambient Temp (25°C)') # Plot the ambient temperature
plt.title("Thermal Response of an Enclosed Chamber") # Set the title of the plot
plt.xlabel("Time (s)") # Set the x-axis label
plt.ylabel("Temperature (°C)") # Set the y-axis label
plt.grid(True) # Add a grid to the plot
plt.legend()# Add a legend to the plot
plt.show() # Display the plot





# Python RK4 Template Code (with ODE for thermal system)

