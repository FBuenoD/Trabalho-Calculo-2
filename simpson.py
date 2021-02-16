import sys
from math import *

def simpson(a, b, n, f):
  sum = 0
  inc = (b - a) / n
  for k in range(n + 1):
    x = a + (k * inc)
    summand = f(x)
    if (k != 0) and (k != n):
      summand *= (2 + (2 * (k % 2)))
    sum += summand
  return ((b - a) / (3 * n)) * sum

if __name__ == '__main__':
    re = simpson(-2, 1, 6, lambda x: e**((-x**2)/2))
    print(re)
