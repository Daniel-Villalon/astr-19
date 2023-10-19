import numpy as np

def loopfunc(xarray, sin_values):
    for i in range(1000):
      print(f"{xarray[i]:.3f} | {sin_values[i]:.3f}")

def main():
    array = np.linspace(0, 2 * np.pi, 1000)
    valuesOFsin = np.sin(array)

    print("x     | sin(x)")
    print("-----------------")

    loopfunc(array, valuesOFsin)
   

if __name__ == "__main__":
    main()