import numpy as np

import constants as cst


class System:
    def __init__(self, num_rep, gamma, a=cst.angstrom2bohr(0.4), C=0.3):

        self.num_rep = num_rep
        self.a = a
        self.C = C
        self.gamma = gamma
        self.V0 = 1 / (2 * cst.m_p * self.a ** 2 * C)
        self.temp = 0.4 * self.V0 / cst.kb
        self.K = self.num_rep * cst.m_p * cst.kb ** 2 * self.temp ** 2

        self.positions = np.zeros(num_rep)
        self.speeds = np.zeros(num_rep)

    def get_temp(self):
        return self.temp

    def get_positions(self):
        return self.positions

    def set_positions(self, positions):
        self.positions = positions

    def get_speeds(self):
        return self.speeds

    def set_speeds(self, speeds):
        self.speeds = speeds

    def kinetic_energy(self):
        return np.sum(
            0.5 * cst.m_p * self.speeds ** 2
            - 0.5 * self.K * (self.positions - np.roll(self.positions, 1)) ** 2
        )

    def potential_energy(self):
        return (1 / self.num_rep) * np.sum(self._V(self.positions))

    def total_energy(self):
        return self.potential_energy() + self.kinetic_energy()

    def centroid_position(self):
        return (1 / self.num_rep) * np.sum(self.positions)

    def forces(self, time_step):
        
        Ir = 2 * cst.m_p * gamma * cst.kb * self.temp

        return -4 * self.V0 * (
            self.positions ** 3 / self.a ** 4 - self.positions / self.a ** 2
        ) + np.sum(
            -self.K
            * (
                2 * self.positions
                - np.roll(self.positions, -1)
                - np.roll(self.positions, 1)
            )
        )
        - cst.m_p * gamma * self.speeds
        + np.sqrt(Ir/time_step) * np.random.normal()

    def _V(self, x):
        return self.V0 * ((x / self.a) ** 2 - 1) ** 2
