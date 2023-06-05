#!/usr/bin/python3
def element_at(my_list, idx):

    for i in my_list:
        if idx > len(my_list) - 1 or idx < 0:
            return None
        if my_list[i] == my_list[idx]:
            return my_list[i]
