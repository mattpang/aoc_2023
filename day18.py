from collections import defaultdict
lines = '''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)'''.splitlines()
lines = open('./input18.txt').read().splitlines()

mesh = defaultdict(dict)
level = 0 
x=0
y=0
allx=[]
ally=[]
points = set()
lookup = {'0':'R','1':'D','2':'L','3':'U'}
part2= True
for line in lines:
    #mesh[level][(x,y)]=colourhex
    d,c,hex = line.split(' ')
    hex,dir = hex[2:-2],hex[-2:-1]
    c = int(c)
    if part2:
        d = lookup[dir]
        c = int(hex,16)

    for step in range(c):
        if d=='D':
            y+=1
        elif d=='U':
            y-=1
        elif d=='L':
            x-=1
        elif d=='R':
            x+=1

        points.add((x,y))
    allx.append(x)
    ally.append(y)

import numpy as np
# https://stackoverflow.com/a/30408825
def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))
A = PolyArea(allx,ally)
b = len(points)

assert(b % 2 == 0)
I = A + 1 - b // 2
print(int(I+b))

