#!/usr/bin/python3
def no_c(my_string):
    void_char = ""
    py_c = "c"
    py_C = "C"
    r_string = ""
    for i in my_string:
        if i == py_c or i == py_C:
            r_string += void_char
        else:
            r_string += i

    return r_string
