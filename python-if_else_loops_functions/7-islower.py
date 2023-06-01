#!/usr/bin/env python3
def islower(c):
    if ord(c) in range(96, 123):
        return True
    elif ord(c) in range(64, 91):
        return False
    else:
        False
