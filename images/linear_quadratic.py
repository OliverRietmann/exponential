#!/usr/bin/python
#-*- coding:utf-8 -*-

#import os
#import sys

import numpy as np
import matplotlib.pyplot as plt

linear_filename = "linear_growth.pdf" #sys.argv[2]
quadratic_filename = "quadratic_growth.pdf" #sys.argv[2]

x = np.linspace(0.0, 10.0, 100)
y = 0.5 * x

plt.figure()
plt.title("Linear Growth")
plt.plot(x, y, label=r"$f(x)=\frac{1}{2}\cdot x$")
plt.xticks(range(11))
plt.xlabel("number of apples")
plt.ylabel("price")
plt.grid(True)
plt.legend(loc="upper left")
plt.tight_layout()
#plt.show()
plt.savefig(linear_filename, bbox_inches='tight')
plt.close()


x = np.linspace(0.0, 10.0, 100)
y = 0.25 * x**2

plt.figure()
plt.title("Quadratic Growth")
plt.plot(x, y, label=r"$f(x)=\frac{1}{4}\cdot x^2$")
plt.xticks(range(11))
plt.yticks([i * 4 for i in range(7)])
plt.xlabel("edge length")
plt.ylabel("area")
plt.grid(True)
plt.legend(loc="upper left")
plt.tight_layout()
#plt.show()
plt.savefig(quadratic_filename, bbox_inches='tight')
plt.close()