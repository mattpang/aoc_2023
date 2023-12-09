lines = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''.splitlines()

import numpy as np 

lines = np.genfromtxt(lines,dtype=int,delimiter=' ')
lines = np.genfromtxt('input9.txt',dtype=int,delimiter=' ')

# # fit a polyline function? might be iffy
# total = 0 
# for line in lines:
#     z = np.polyfit(x=range(len(line)),y=line,deg=40)
#     p = np.poly1d(z)
#     print(p)
#     total+=np.round(p(len(line)),0)
# print(int(total))


def differences(row):
    diffs = row[1:]-row[:-1]
    if (diffs == 0).all(): 
        return row[-1]
    else:
        return row[-1]+differences(diffs)

total = 0 
for line in lines.copy():
    total+=differences(line)

print(total)

total = 0 
for line in lines.copy():
    total+=differences(line[::-1])

print(total)