# Quadratic interpolation of Direct method

import numpy as np


def direct(t):
    sum = 0
    T = np.linalg.solve(A, V)
    print("\nv(t) = %g" %T[0], "+ %gt" %T[1], "+ %gt^2" %T[2])
    
    for i in range(3):
        sum += (T[i] * t ** i)
    
    print("v(%g) =" %t, "%g" %sum)
    return

    
# Main code starts from here

A = np.array([[1, 10, 100],
              [1, 15, 225],
              [1, 20, 400]])
V = np.array([[227.04],
              [362.78],
              [517.35]])

t = float(input("Enter t = "))
direct(t)


"""
Enter t = 16

v(t) = 12.05 + 17.733t + 0.3766t^2
v(16) = 392.188
"""