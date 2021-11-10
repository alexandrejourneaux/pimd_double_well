import numpy as np
from matplotlib import pyplot as plt

cm2in = 1.0/2.54

#Direct input
data = np.loadtxt("positions.dat")
data = data.flatten()

hist, bin_edges = np.histogram(data,bins=100,density=True)
bin_centers = np.zeros(len(hist))
for i in range(len(hist)):
    bin_centers[i] = 0.5*(bin_edges[i]+bin_edges[i+1])

plt.figure()
plt.xlabel('Position (\AA{})')
plt.ylabel('Probability density (1/\AA{})')
plt.plot(bin_centers,hist,ls='-',lw=2)
plt.tight_layout(pad=0.2)
plt.savefig("proba.png")
