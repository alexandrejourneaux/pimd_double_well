import numpy as np
import constants as cst
from verlet import simulation
from output import write_out

a = cst.angstrom2bohr(0.4)
print("a=",a,"bohr","=",cst.bohr2angstrom(a),"Angstrom")
C = 0.3
print("C=",C)
time_step = 4.0
print("dt=",time_step,"a.u","=",cst.au2fs(time_step),"fs")
tf = 80000
print("nstep=",tf)
nb_repro = 1
print("Trotter nb=",nb_repro)
pos_init = 0.0
print("Initial position=",pos_init, "bohr")

gamma_list = np.logspace(-3, 0, 10)
temp_list = []
for gamma in gamma_list:
    position, speed, energy, pot_energy, kin_energy, mean_kin_energy, mean_pot_energy = simulation(time_step, tf, nb_repro, pos_init, gamma, a, C)
    temp_list.append(2 * mean_kin_energy[-1] / cst.kb)
    print("temp obtained=", temp_list[-1], "K")

f = open('gamma_det.dat','w')
for i in range(len(gamma_list)):
    f.write(str(gamma_list[i])+" ")
    f.write(str(temp_list[i]))
    f.write("\n")
f.close()
