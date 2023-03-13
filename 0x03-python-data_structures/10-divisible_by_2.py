#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div_2_list = []
    for i in my_list:
        if i % 2 == 0:
            div_2_list.append(True)
        else:
            div_2_list.append(False)
    return div_2_list
