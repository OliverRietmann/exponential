#!/usr/bin/python
#-*- coding:utf-8 -*-

#import os
#import sys

import numpy as np
import matplotlib.pyplot as plt

linear_filename = "linear_growth.pdf" #sys.argv[2]
quadratic_filename = "quadratic_growth.pdf" #sys.argv[2]

def skip(gen, step):
    return (step * (i // step) for i in gen)
step = 10

x = np.linspace(0.0, 8.0, 81)
y = 20 * x + 50
x_triangle = np.array([x[k] for k in skip(range(1, len(x)), step)])
y_triangle = np.array([y[k] for k in skip(range(0, len(y) - 1), step)])

plt.figure()
plt.title("Money on the Bank account")
plt.plot(x, y, label=r"$f(x)=20x+50$")
plt.plot(x_triangle, y_triangle, label=r"bank account")
plt.xlim(0, 8)
plt.ylim(0, 200)
plt.xticks(range(9))
#plt.yticks(range(0, 101, 10))
plt.xlabel("year")
plt.ylabel("CHF")
plt.grid(True)
plt.legend(loc="upper left", prop={'size': 14})
plt.tight_layout()
#plt.show()
plt.savefig(linear_filename, bbox_inches='tight')
plt.close()


y = 50 * 1.20**x
x_triangle = np.array([x[k] for k in skip(range(1, len(x)), step)])
y_triangle = np.array([y[k] for k in skip(range(0, len(y) - 1), step)])

plt.figure()
plt.title("Quadratic Growth")
plt.plot(x, y, label=r"$f(x)=50\cdot 1.2^x$")
plt.plot(x_triangle, y_triangle, label=r"bank account")
plt.xlim(0, 8)
plt.ylim(0, 200)
plt.xticks(range(9))
#plt.yticks(range(0, 101, 10))
plt.xlabel("year")
plt.ylabel("CHF")
plt.grid(True)
plt.legend(loc="upper left", prop={'size': 14})
plt.tight_layout()
#plt.show()
plt.savefig(quadratic_filename, bbox_inches='tight')
plt.close()
