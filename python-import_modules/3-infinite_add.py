#!/usr/bin/python3
import sys
if __name__ == "__main__":
    resultado = 0
    for i in range(1, len(sys.argv)):
        resultado = resultado + int(sys.argv[i])
    print(resultado)
