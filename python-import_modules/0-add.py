#!/usr/bin/python3
from add_0 import add  # Desde el archivo add_0 importar la funcion add
if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
