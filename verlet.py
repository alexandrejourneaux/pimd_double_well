import numpy as np
import constants as cst

def random_speeds(num_rep, temp):
    dzeta_1 = np.random(num_rep)
    dzeta_2 = np.random(num_rep)
    v0 = np.sqrt(cst.Boltzmann * temp / m)
    dzeta = np.sqrt(2) * np.cos(2 * np.pi * dzeta_1) * np.sqrt(-np.log(dzeta_2))
    return v0 * dzeta

def is_valid_integration(former_energy, new_energy):
    return np.abs(former_energy - new_energy) / new_energy < 1e-4
    
def simulation(time_step, t_f, num_rep, a, C):
    
    system = System(num_rep, a, C)
    system.set_positions(np.sqrt(2) * a * np.random())
    
    positions_list = [system.get_positions()]
    speeds_list = [system.get_speeds()]
    total_energy_list = [system.total_energy()]
    t = time_step 
     
    system.set_positions(system.get_positions() + time_step**2 / 2 * system.forces() / cst.m_p)
    system.set_speeds((system.get_positions() - positions_list[0]) / time_step)

    positions_list.append([system.get_positions()])
    speeds_list.append([system.get_speeds()])
    total_energy_list.append([system.total_energy()])
    niter = np.int(tf / time_step)
    
    for i in range(1, niter):
        
        system.set_positions(2 * system.get_positions() - positions_list[-1] + time_step**2 * system.forces())
        system.set_speeds((system.get_positions() - positions_list[-1]) / (2 * time_step))
        
        positions_list.append([system.get_positions()])
        speeds_list.append([system.get_speeds()])
        total_energy_list.append([system.total_energy()])
        if not is_valid_integration(total_energy_list[-2], total_energy_list[-2]):
            raise ValueError("Time step too big")
    
    return positions_list, speeds_list, total_energy_list

