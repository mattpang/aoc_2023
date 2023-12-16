lines = open('example16.txt','r').read().splitlines()
lines = open('input16.txt','r').read().splitlines()
# each tile is stored as a tuple 3 number, 
# if its already in the set, then don't need to track again.
# 
# 
import numpy as np
from collections import Counter
import sys 
global seen

sys.setrecursionlimit(10000)


def path(c,dir):
    if c=='.':
        return [dir]
    elif c=='/':
        if dir == (1,0):
            return [(0,-1)]
        elif dir == (-1,0):
            return [(0,1)]
        elif dir == (0,-1):
            return [(1,0)]
        elif dir == (0,1):
            return [(-1,0)]
    elif c=='\\':
        if dir == (1,0):
            return [(0,1)]
        elif dir == (-1,0):
            return [(0,-1)]
        elif dir == (0,-1):
            return [(-1,0)]
        elif dir == (0,1):
            return [(1,0)]
    elif c=='-':
        if dir == (1,0):
            return [(1,0)]
        elif dir == (-1,0):
            return [(-1,0)]
        elif dir == (0,-1):
            return [(1,0),(-1,0)]
        elif dir == (0,1):
            return [(1,0),(-1,0)]
    elif c=='|':
        if dir == (0,1):
            return [(0,1)]
        elif dir == (0,-1):
            return [(0,-1)]
        elif dir == (1,0):
            return [(0,1),(0,-1)]
        elif dir == (-1,0):
            return [(0,1),(0,-1)]
    else:
        print(c,dir)
        raise ValueError

def follow(tile):
    global seen
    if tile in seen:
        return
    else:
        seen.add(tile)
        x,y = tile[2]
        nx = tile[0]+x
        ny = tile[1]+y
        if (nx >= len(lines[0])) or (nx<0):
            return 
        if (ny >= len(lines)) or (ny<0):
            return 
        try:
            c = lines[ny][nx]
        except IndexError:
            print(ny)
            exit()
        nexttile = []
        # print(c,nx,ny,tile[2])
        for p in path(c,tile[2]): 
            nexttile.append((nx,ny,p))

        for n in nexttile:
            follow(n)
    
def solve(s=(0,0),dir=(1,0)):
    global seen
    seen = set()
    if lines[s[0]][s[1]]=='.':
        follow((s[0],s[1],dir))
    else:
        seen.add((s[0],s[1],dir))
        for p in path(lines[s[1]][s[0]],dir):
            # print(p)
            start = (s[0]+p[0],s[1]+p[1],p)
            follow(start)

    g = np.zeros((len(lines),len(lines[0])),dtype=int)
    locs = set()
    for s in seen:
        g[s[0],s[1]] = 1
        locs.add((s[0],s[1]))
    # print(g.T)
    # np.savetxt(sys.stdout, g.T,fmt='%i',delimiter='')
    return len(locs)

print(solve()) # part 1 6361

#part2
gsize = len(lines)
# print(gsize)
spoints = []
for i in range(gsize):
    spoints.append((i,0,(0,1)))# top
    spoints.append((i,gsize-1,(0,-1)))# bottom
    spoints.append((0,i,(1,0)))# left
    spoints.append((gsize-1,i,(-1,0)))# right
mscore = 0 
for point in spoints:
    score = solve((point[0],point[1]),point[2])
    if score>mscore:
        mscore=score
        best_tile = point
print(mscore,best_tile)