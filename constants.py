from scipy.constants import Boltzmann, hbar, m_p

a = 0.04
C = 0.3
V0 = hbar ** 2 / (2 * m_p * a ** 2 * C)
T = 0.4 * V0 / Boltzmann
