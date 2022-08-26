#!/usr/bin/python
#-*- coding:utf-8 -*-

#import os
#import sys

import numpy as np
import matplotlib.pyplot as plt

filename = "explog.pdf" #sys.argv[1]

x = np.linspace(-24, 24, 1000)

f = lambda t: 440.0 * 2**(t / 12)

plt.figure()
plt.title("$f(x)=b^x$")
plt.plot(x, f(x), label=r"$f(x)=440\cdot 2^{t/12}$")
plt.xlabel(r"$octaves$")
plt.ylabel(r"$frequency (Hz)$")
plt.xlim([-24,24])
#plt.ylim([-4.0, 4.0])
#ax = plt.gca()
#ax.set_aspect('equal', adjustable='box')
#plt.axes(aspect='equal', adjustable='box')
plt.grid(True)
plt.legend(loc="upper left", prop={'size': 16})
plt.tight_layout()
plt.savefig(filename, bbox_inches='tight')
plt.close()
