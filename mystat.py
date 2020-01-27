from math import exp, log, pi, sqrt, cos, sin 
import random as rd


def norm_pdf(x):
    """Standard normal probability density function"""
    return (1.0/((2*pi)**0.5))*exp(-0.5*x*x)

def norm_cdf(x):
    """An approximation to the cumulative distribution function for the standard normal distribution:
    N(x) = \frac{1}{sqrt(2*\pi)} \int^x_{-\infty} e^{-\frac{1}{2}s^2} ds"""
    k = 1.0/(1.0+0.2316419*x)
    k_sum = k*(0.319381530 + k*(-0.356563782 + k*(1.781477937 + k*(-1.821255978 + 1.330274429*k))))

    if x >= 0.0:
        return (1.0 - (1.0/((2*pi)**0.5))*exp(-0.5*x*x) * k_sum)
    else:
        return 1.0 - norm_cdf(-x)
      
      
      
      
      
def box_muller():
  u1=rd.random()
  u2=rd.random()
  z0=sqrt(-2*log(u1))*cos(2*pi*u2)
  z1=sqrt(-2*log(u1))*sin(2*pi*u2)
  return z0