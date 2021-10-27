import numpy as np
import constants as cst
from verlet import simulation
import matplotlib.pyplot as plt

a = cst.angstrom2bohr(0.4)
C = 0.3
time_step = 1e-3
tf = 1e-1
position, speed, energy, pot_energy, kin_energy = simulation(1, 10000, 1, a)

plt.figure(1)
plt.plot(position)

plt.figure(2)
plt.plot(speed)

plt.figure(3)
plt.plot(energy)
plt.plot(pot_energy)
plt.plot(kin_energy)
plt.show()
