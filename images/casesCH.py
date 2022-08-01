#!/usr/bin/python
#-*- coding:utf-8 -*-

import csv
#import os
#import sys

import numpy as np
import matplotlib.pyplot as plt

csv_filename = "casesCH.csv" #sys.argv[1]
image_filename = "casesCH.pdf" #sys.argv[2]

def exponential(x, r):
	return 2.0**(r * x)

full_data = np.genfromtxt('casesCH.csv', delimiter='\n')
full_t = np.arange(len(full_data)) + 1

data = full_data[200:250] #[600:700] 
t = np.arange(len(data))
fit = 80.0 * exponential(t, 1.0 / 6.0)

a = 10
b = -12
y_fit = np.log2(data[a:b])
x_fit = t[a:b]
c = np.polyfit(x_fit, y_fit, 1)

y = 2**(c[0] * t + c[1])
print("regression:", c[0], c[1])
print("prefactor:", 2**c[1])
print("doubling time:", 1.0 / c[0], 1.0 / 6.0)

plt.figure()
plt.title("Confirmed Covid Infections in Switzerland (Starting September 2020)")
plt.plot(t, data, 'c.', label="7-days average reported by BAG")
plt.plot(t, fit, 'r-', label=r"$f(x)=80\cdot 2^{x/6}$")
plt.xticks(range(0, 50, 6))
plt.xlabel("days")
plt.ylabel("covid infections")
plt.ylim((0,9000))
plt.grid(True)
plt.legend(loc="upper left")
plt.tight_layout()
#plt.show()
plt.savefig(image_filename, bbox_inches='tight')
plt.close()
