from scipy.constants import hbar, m_p, Boltzmann

a = 0.04
C = 0.3
V0 = hbar**2 / (2 * m_p * a**2 * C)
T = 0.4 * V0 / Boltzmann