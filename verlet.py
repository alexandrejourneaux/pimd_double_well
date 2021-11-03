import numpy as np
import constants as cst
from system import System


def random_speeds(num_rep, temp):
    dzeta_1 = np.random(num_rep)
    dzeta_2 = np.random(num_rep)
    v0 = np.sqrt(cst.Boltzmann * temp / m)
    dzeta = np.sqrt(2) * np.cos(2 * np.pi * dzeta_1) * np.sqrt(-np.log(dzeta_2))
    return v0 * dzeta


def is_valid_integration(former_energy, new_energy):
    return np.abs(former_energy - new_energy) / new_energy < 1e-4


def simulation(time_step, t_f, num_rep, pos_init, gamma, a=cst.angstrom2bohr(0.4), C=0.3):
    
    sys = System(num_rep, gamma, a, C)
    print("Initial temp :", sys.get_temp())
    sys.set_positions(pos_init)

    positions_list = [sys.get_positions()]
    speeds_list = [sys.get_speeds()]
    total_energy_list = [sys.total_energy()]
    potential_energy_list = [sys.potential_energy()]
    kinetic_energy_list = [sys.kinetic_energy()]

    sys.set_positions(sys.get_positions() + time_step ** 2 / 2 * sys.forces(time_step) / cst.m_p)
    sys.set_speeds((sys.get_positions() - positions_list[0]) / time_step)

    positions_list.append(sys.get_positions())
    speeds_list.append(sys.get_speeds())
    total_energy_list.append(sys.total_energy())
    potential_energy_list.append(sys.potential_energy())
    kinetic_energy_list.append(sys.kinetic_energy())
    niter = np.int(t_f / time_step)

    for i in range(1, niter):

        sys.set_positions(
            2 * sys.get_positions() - positions_list[-2] + time_step ** 2 * sys.forces(time_step) / cst.m_p
        )
        sys.set_speeds((sys.get_positions() - positions_list[-2]) / (2 * time_step))

        positions_list.append(sys.get_positions())
        speeds_list.append(sys.get_speeds())
        total_energy_list.append(sys.total_energy())
        potential_energy_list.append(sys.potential_energy())
        kinetic_energy_list.append(sys.kinetic_energy())
        #if not is_valid_integration(total_energy_list[-2], total_energy_list[-1]):
         #   raise ValueError("Time step too big")

    return positions_list, speeds_list, total_energy_list, potential_energy_list, kinetic_energy_list

