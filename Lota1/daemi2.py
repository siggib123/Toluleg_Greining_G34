import matplotlib.pyplot as mpl
import numpy as np

def f(x):
    return 2*x**4 + 23*x**3 + 45*x**2 + 60*x + 50

def Df(x):
    return 8*x**3 + 69*x**2 + 90*x + 60



def adferd_newtons(I_guess, tolerance):
    x = I_guess
    x_old = x + 10*tolerance  # bara til að komast inn í lykkjuna
    
    while abs(x - x_old) > tolerance:
        x_old = x
        x = x_old - f(x_old) / Df(x_old)

    return x



I_GUESS = -1 + 2j
TOLERANCE = 1e-10

root = adferd_newtons(I_GUESS, TOLERANCE)
print("Niðurstaða Newtons:", root) 
