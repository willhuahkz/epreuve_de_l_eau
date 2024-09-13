"""
Module to print sequence of two numbers
"""

#print(f"{hour:02}:{minute:02}")
list_nbr = [0, 1]
res_str = ''
offset = 2

while list_nbr[0] < 99 and list_nbr[1] < 100:
    res_str += f'{list_nbr[0]:02} {list_nbr[1]:02} '
    list_nbr[1] += 1
    if list_nbr[1] == 100:
        list_nbr[1] = 0 + offset
        offset += 1
        list_nbr[0] += 1

print(res_str)
