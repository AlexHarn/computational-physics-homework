import numpy as np
import matplotlib.pyplot as plt
import os


for file in os.listdir():
    if file.endswith(".dat"):
        r, x = np.genfromtxt(file, unpack=True)
        plt.xlim(min(r), max(r))
        plt.plot(r, x, '.', ms=0.1)
        plt.xlabel(r"$r$")
        plt.ylabel(r"$x$")
        plt.savefig(file[:-4]+".pdf")
        plt.clf()
