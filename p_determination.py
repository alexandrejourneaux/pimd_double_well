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
nb_repro = 4
print("Trotter nb=",nb_repro)
pos_init = 0.0
print("Initial position=",pos_init, "bohr")
gamma = 0.001
print("Gamma=",gamma,"a.u","=",gamma/0.0241888432650478,"1/fs","=",1e3*gamma/0.0241888432650478,"THz")

P_list = np.arange(1, 11)
mean_energy_list = []
for P in P_list:
    position, speed, energy, pot_energy, kin_energy, mean_kin_energy, mean_pot_energy = simulation(time_step, tf, P, pos_init, gamma, a, C)
    mean_energy_list.append(mean_kin_energy[-1] + mean_pot_energy[-1])
    print("energy obtained=", mean_energy_list[-1])

f = open('P_det.dat','w')
for i in range(len(P_list)):
    f.write(str(P_list[i])+" ")
    f.write(str(mean_energy_list[i]))
    f.write("\n")
f.close()
