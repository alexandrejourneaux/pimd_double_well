#Values in SI units
me_SI = 9.1093837015* 1e-31  # electron mass
a0_SI = 5.29177210903* 1e-11  # Bohr radius
hbar_SI = 1.054571817 * 1e-34  # J.s

def angstrom2bohr(x):
    return x / a0_SI * 1e-10

def bohr2angstrom(x):
    return x * a0_SI / 1e-10

kb = 3.166689e-6  # Ha/K
m_p = 1836.15267343  # me
