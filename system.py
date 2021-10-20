import numpy as np

import constants as cst


class System:

    def __init__(self, num_rep, a=0.04, C=0.3):

        self.num_rep = num_rep
        self.a = a
        self.C = C
        self.V0 = cst.hbar ** 2 / (2 * cst.m_p * a ** 2 * C)
        self.temp = 0.4 * cst.V0 / cst.Boltzmann
        self.K = (
            self.num_rep * cst.m_p * cst.Boltzmann ** 2 * self.temp ** 2
        ) / cst.hbar ** 2

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

    def forces(self):
        return 4 * self.V0 * (self.positions ** 3 / a ** 4 - x / a ** 2) + np.sum(
            -self.K
            * (
                2 * self.positions
                - np.roll(self.positions, -1)
                - np.roll(self.positions, 1)
            )
        )

    def _V(self, x):
        return self.V0 * ((x / self.a) ** 2 - 1) ** 2
