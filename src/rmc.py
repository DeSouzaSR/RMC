"""
This program performs the calculation of the Radial Mass Concentration (RMC)
of the Solar System according to the article by Chambers, 2001

By Sandro Ricardo De Souza
2023-07-03
"""

import numpy as np
import matplotlib.pyplot as plt

# Mass of the inner planets
m = np.array([0.0553, 0.815, 1.0, 0.107])

# Semimajor axis of the inner planets
a = np.array([0.387, 0.723, 1.0, 1.52])

# Range under analysis
range_ss = np.linspace(0.1, 1.6, 1000)

# Calculations
sum_mass = np.sum(m)
sum_den = 0.0
for i in range(len(m)):
    sum_den = sum_den + m[i] * (np.log10(range_ss/a[i]))**2
RMC_list = sum_mass/sum_den 
RMC = max(RMC_list)
print('Valor de RMC = {0:0.1f}'.format(RMC))

#Plot
plt.figure(figsize=(5,4))
plt.xlabel('Semimajor axis [au]')
plt.ylabel('RMC')
plt.title("RMC Inner Planets")
plt.annotate('RMC: {:0.1f}'.format(RMC), xy=(0.2,80))
plt.plot(range_ss, RMC_list)
plt.scatter(a, [0]*len(a), s=m*500)
plt.savefig("figures/rmc_innerplanets.png")
plt.show()
