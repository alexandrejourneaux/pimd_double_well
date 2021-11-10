import numpy as np

import constants as cst


class System:
    def __init__(self, num_rep, gamma, a=cst.angstrom2bohr(0.4), C=0.3):

        self.num_rep = num_rep
        self.a = a
        self.C = C
        self.gamma = gamma
        self.V0 = 1 / (2 * cst.m_p * self.a ** 2 * C)
        print("V0=",self.V0,"Ha","=",cst.hartree2ev(self.V0),"eV")
        self.temp = 0.4 * self.V0 / cst.kb
        print("T=",self.temp,"K")
        self.K = self.num_rep * cst.m_p * cst.kb ** 2 * self.temp ** 2

        self.positions = np.zeros(num_rep)
        self.speeds = np.zeros(num_rep)

    def get_temp(self):
        return self.temp

    def get_positions(self):
        return self.positions

    def set_positions(self, positions):
        self.positions = np.array(positions)

    def get_speeds(self):
        return self.speeds

    def set_speeds(self, speeds):
        self.speeds = np.array(speeds)

    def kinetic_energy(self):
        kin = 0.5*cst.m_p*np.sum(self.speeds**2)
        kin = kin - 0.5*self.K*np.sum((self.positions - np.roll(self.positions,1))**2)
        return kin

    def potential_energy(self):
        return (1 / self.num_rep) * np.sum(self._V(self.positions))

    def total_energy(self):
        return self.potential_energy() + self.kinetic_energy()

    def centroid_position(self):
        return (1 / self.num_rep) * np.sum(self.positions)

    def forces(self, time_step):

        Ir = 2 * cst.m_p * self.gamma * cst.kb * self.temp

        y = self.positions / self.a
        f_pot = -4.0*self.V0*(y**3-y)/self.a/self.num_rep
        f_harm = -self.K*(2.0*self.positions - \
                  np.roll(self.positions, -1) - np.roll(self.positions, 1))
        f_lang = -cst.m_p*self.gamma*self.speeds \
                 + np.sqrt(Ir / time_step)*np.random.normal(size=(self.num_rep,))

        return f_pot + f_harm + f_lang

    def _V(self, x):
        return self.V0 * ((x / self.a) ** 2 - 1) ** 2
