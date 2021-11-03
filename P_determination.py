import numpy as np
import constants as cst
from verlet import simulation
import matplotlib.pyplot as plt

"""
Finding the optimal time step for the simulation: we want delta E / E small enough
We choose a time step of 1.
"""
a = cst.angstrom2bohr(0.4)
C = 0.3
time_step = 1
t_f = 10000
gamma = 0

for time_step in np.logspace(3, -3, 7):
    position, speed, energy, pot_energy, kin_energy = simulation(time_step, t_f, nb_repro, 0.5*a, 0)
    delta_energy = np.max(energy) - np.min(energy)
    print("Time step:", time_step, "energy relative variation", delta_energy / energy[0])
