#!/usr/bin/python3
class MyList(list):
    
    def __init__(self):
        pass

    def print_sorted(self):
        s_list = sorted(self)
        print(s_list)
