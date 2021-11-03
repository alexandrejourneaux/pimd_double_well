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

ii = 0
for gamma in np.linspace(0.01, 1.0, 10): #np.logspace(6, -6, 13):
    position, speed, energy, pot_energy, kin_energy, mean_kin_energy = simulation(time_step, tf, nb_repro, pos_init, gamma)
    print("Final temp : "+ str(2*np.mean(kin_energy)/cst.kb))

    time = [i*time_step for i in range(int(tf/time_step) + 1)]

    plt.figure(ii+1)
    plt.plot(time, position)
    plt.xlabel("Time")
    plt.ylabel("Position")
    plt.title("Evolution of position over time")
    plt.savefig("position"+str(int(np.log10(gamma))))
    
    plt.figure(ii+2)
    plt.plot(time, speed)
    plt.xlabel("Time")
    plt.ylabel("Speed")
    plt.title("Evolution of speed over time")
    plt.savefig("speed"+str(int(np.log10(gamma))))
    
    plt.figure(ii+3)
    plt.plot(time[:-1], mean_kin_energy)
    plt.xlabel("Time")
    plt.ylabel("Energy")
    plt.title("Evolution of mean energy over time")
    plt.savefig("speed"+str(int(np.log10(gamma))))

    plt.figure(ii+4)
    plt.plot(time, energy, label="total")
    plt.plot(time, pot_energy, label="potential")
    plt.plot(time, kin_energy, label="kinetic")
    plt.title("Evolution of total, potential and kinetic energy over time")
    plt.xlabel("Time")
    plt.ylabel("Energy")
    plt.legend()
    plt.savefig(f"energy_{int(np.log10(gamma))}")
    ii+=4
    plt.show()
