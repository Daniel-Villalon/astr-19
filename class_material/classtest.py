import sys 
import numpy as np

def main():
  x = 0.0
  for i in range(0, 20):
    x = (i * 2) + 19.0
    print(f'{i} The value of x is =', x)


if __name__== "__main__":
  main()