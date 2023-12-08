import sys
import numpy as np

def main():
  x = 0.0

  for i in range(0, 20):
    x = i
    print(f'the value of x is = {(x * 2) + 19.0}')

if __name__=='__main__':
  main()