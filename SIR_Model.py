# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 12:08:07 2022

@author: AYLIN KAYA
"""

import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt

def SIR_model(y, t, beta, gamma):
  S, I, R = y

  dS_dt = -beta*S*I
  dI_dt = beta*S*I - gamma*I
  dR_dt = gamma*I

  return([dS_dt,dI_dt,dR_dt])

S0 = 0.995
I0 = 0.005
R0 = 0.0
beta = 0.35
gamma = 0.1

t = np.linspace(0,100,10000)

solution = scipy.integrate.odeint(SIR_model, [S0, I0, R0], t, args=(beta, gamma))

solution = np.array(solution)

plt.figure(figsize=[8,4])
plt.plot(t, solution[:,0], label="S(t)", linewidth=3, color='#FFA500')
plt.plot(t, solution[:,1], label="I(t)", linewidth=3, color='#FF0000')
plt.plot(t, solution[:,2], label="R(t)", linewidth=3, color='#1E90FF')
plt.grid()
plt.legend()
plt.xlabel("Time(Day)")
plt.ylabel("Population")
plt.title("SIR Model")
plt.show()
