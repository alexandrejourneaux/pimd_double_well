import numpy as np
import constants as cst
from verlet import simulation
import matplotlib.pyplot as plt

a = cst.angstrom2bohr(0.4)
C = 0.3
time_step = 1
tf = 10000
nb_repro = 1
pos_init = a
gamma = 0.100

#for time_step in np.logspace(6, -6, 13):
position, speed, energy, pot_energy, kin_energy = simulation(time_step, tf, nb_repro, pos_init, gamma)

time = [i*time_step for i in range(int(tf/time_step) + 1)]

plt.figure(1)
plt.plot(time, position)
plt.xlabel("Time")
plt.ylabel("Position")
plt.title("Evolution of position over time")

plt.figure(2)
plt.plot(time, speed)
plt.xlabel("Time")
plt.ylabel("Speed")
plt.title("Evolution of speed over time")

plt.figure(3)
plt.plot(time, energy, label="total")
plt.plot(time, pot_energy, label="potential")
plt.plot(time, kin_energy, label="kinetic")
plt.title("Evolution of total, potential and kinetic energy over time")
plt.xlabel("Time")
plt.ylabel("Energy")
plt.legend()
plt.show()
