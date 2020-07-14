from itertools import groupby 

input_string = input()
a = [list(g) for k, g in groupby(input_string)]
for i in a:
    occ = str(len(i))
    print('(' + occ + ', ' + i[0] + ')', end=" ")
