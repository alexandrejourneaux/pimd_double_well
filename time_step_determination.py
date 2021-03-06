import numpy as np
import constants as cst
from verlet import simulation
import matplotlib.pyplot as plt

"""
Finding the optimal time step for the simulation: we want delta E / E small enough
We choose a time step of 1.
"""
a = cst.angstrom2bohr(0.4)
print("a=",a,"bohr","=",cst.bohr2angstrom(a),"Angstrom")
C = 0.3
print("C=",C)
time_step = 4.0
print("dt=",time_step,"a.u","=",cst.au2fs(time_step),"fs")
tf = 80000
print("nstep=",tf)
nb_repro = 4
print("Trotter nb=",nb_repro)
pos_init = 1.05*a 
print("Initial position=",pos_init, "bohr")
gamma = 0
print("Gamma=",gamma,"a.u","=",gamma/0.0241888432650478,"1/fs","=",1e3*gamma/0.0241888432650478,"THz")

delta_energy = []
for time_step in np.logspace(3, -2, 6):
    position, speed, energy, pot_energy, kin_energy, mean_kin_energy, mean_pot_energy = simulation(time_step, tf, nb_repro, pos_init, gamma, a, C)
    delta_energy.append((np.max(energy) - np.min(energy)) / energy[0])
    print("Time step:", time_step, "energy relative variation", delta_energy[-1])

plt.plot(np.logspace(3, -2, 6), delta_energy)
