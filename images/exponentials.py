#!/usr/bin/python
#-*- coding:utf-8 -*-

#import os
#import sys

import numpy as np
import matplotlib.pyplot as plt

filename_grow = "exponentials_grow.pdf" #sys.argv[1]
filename_decay = "exponentials_decay.pdf" #sys.argv[2]

def f(x, a, b):
    return a * b**x

x = np.linspace(-5.0, 5.0, 100)
a = 1.0

b_list = [4.0, 3.0, 2.0]
b_label = ["$b=4$", "$b=3$", "$b=2$"]
plt.figure()
plt.title("$f(x)=b^x$")
for b, label in zip(b_list, b_label):
    y = f(x, a, b)
    plt.plot(x, y, label=label)
plt.xlabel(r"$x$")
plt.ylabel(r"$f(x)$")
plt.xlim([-5.0, 5.0])
plt.ylim([-5.0, 5.0])
ax = plt.gca()
ax.set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend(loc="upper left", prop={'size': 16})
plt.tight_layout()
plt.savefig(filename_grow, bbox_inches='tight')
plt.close()

b_list = [1.0 / b for b in b_list]
b_label = [r"$b=\frac{1}{2}$", r"$b=\frac{1}{3}$", r"$b=\frac{1}{4}$"]
plt.figure()
plt.title("$f(x)=b^x$")
for b, label in zip(b_list, b_label):
    y = f(x, a, b)
    plt.plot(x, y, label=label)
plt.xlabel(r"$x$")
plt.ylabel(r"$f(x)$")
plt.grid(True)
plt.legend(loc="upper right", prop={'size': 16})
plt.tight_layout()
plt.savefig(filename_decay, bbox_inches='tight')
plt.close()
