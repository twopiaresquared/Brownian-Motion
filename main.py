import mystat as st
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, exp

def GBM_path(S0, mu, sigma, T, n_steps):
  dt = T/n_steps
  val = np.zeros(n_steps)
  val[0]=S0
  for i in range(1,n_steps):
    val[i]=val[i-1]*exp((mu-(sigma*sigma)/2)*dt+sigma*sqrt(dt)*st.box_muller())
  return val
  
mypath = GBM_path(100, 0.1, 0.3, 1, 100)

plt.plot(mypath)
plt.show()