#!/usr/bin/python
#-*- coding:utf-8 -*-

#import os
#import sys

import numpy as np
import matplotlib.pyplot as plt

filename = "decibel.pdf" #sys.argv[1]

f = lambda x: 2.0e-5 * 1.122**x
x = np.linspace(60.0, 100.0, 1000)
y = f(x)

t = np.arange(60, 105, 5)

plt.figure()
plt.title("Perceived Loudness vs. Sound Pressure")
plt.vlines(t, f(x[0]), f(t), linestyle="dashed", color='gray')
plt.hlines(f(t), x[0], t, linestyle="dashed", color='gray')
plt.plot(x, y, label=r"$f(x)=p_0\cdot 1.122^x$")
plt.xlabel(r"dB (decibel)")
plt.ylabel(r"Pa (Pascal)")
plt.xticks(t)
plt.yticks(f(t[4:]))
plt.legend(loc="upper left", bbox_to_anchor=(0.02, 0.9), prop={'size': 16})
plt.tight_layout()
plt.savefig(filename, bbox_inches='tight')
plt.close()
