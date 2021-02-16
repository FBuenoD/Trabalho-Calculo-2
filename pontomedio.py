import sys
from math import *

def midpoint(a, b, n, f):
  sum = 0
  x_int = ((2 * n + 1) * a - b) / (2 * n)
  inc = (b - a) / n
  for k in range(1, n + 1):
    x = x_int + (k * inc)
    sum += f(x)
  return (sum * inc)

if __name__ == '__main__':
    re = midpoint(-1/2,0,4,lambda x: (1/(x**2))*(e**(-1/(2*x**2))))
    print(re)
