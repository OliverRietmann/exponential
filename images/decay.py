#!/usr/bin/python
#-*- coding:utf-8 -*-

#import os
#import sys

import numpy as np
import matplotlib.pyplot as plt

filename = "decay.pdf" #sys.argv[2]

t = 5730.0
f = lambda x: 1024.0 * 2.0**(-x / 5730.0)

x = np.linspace(0.0, 4.0e4, 400)
y = f(x)

years = t * np.arange(7)
z = f(years)

plt.figure()
plt.title("Radioactive Decay of C-14 Atoms")
plt.plot(x, y) # , label=r"$f(x)=a\cdot 2^{-x/t}$"
plt.plot(years, z, 'ro')
plt.xlabel("years")
plt.ylabel("number of C-14 atoms")
plt.grid(True)
#plt.legend(loc="upper left", prop={'size': 14})
plt.tight_layout()
#plt.show()
plt.savefig(filename, bbox_inches='tight')
plt.close()
