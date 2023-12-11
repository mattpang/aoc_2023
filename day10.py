import networkx as nx
import numpy as np
import tqdm
file= '10.txt'
file = 'input10.txt'
# file = '10simple.txt'
# file = 'junk.txt'

m= np.genfromtxt(file,delimiter=1, dtype=str)
print(m)
g = nx.Graph()
connections = 'S|-LJ7F'
connection = {'|':[(0,-1),(0,1)],'-':[(-1,0),(1,0)],'L':[(0,-1),(1,0)],'J':[(0,-1),(-1,0)],'7':[(0,1),(-1,0)],'F':[(0,1),(1,0)]}
compatiable = {'|':'LJ7F|','-':'LJ7F-'}
spos = np.where(m=='S')
spos = (spos[0][0],spos[1][0])
print(spos)
print(m[spos[0]-1:spos[0]+2,spos[1]-1:spos[1]+2])
if file == 'input10.txt':
    Spipe = '|'
elif file == '10.txt':
    Spipe = 'F'
elif file == '10simple.txt':
    Spipe = 'F'
elif file=='junk.txt':
    Spipe = '7'
else:
    raise ValueError

connection['S'] = connection[Spipe]

g.add_node(spos[::-1])

# # not veru efficent
# for i in range(20):
#     for y,row in enumerate(m):
#         for x,pos in enumerate(row):
#             if (pos in connections) and ((x,y) in g.nodes):
#                 for u,v in connection[pos]:
#                     # print(pos,(x,y),(u,v),m[y+v,x+u])
#                     g.add_edge((x,y),(x+u,y+v))
#                     g.add_node((x,y))
#                     g.add_node((x+u,y+v))

# better to have a queue of nodes we need to travel
todo = [spos[::-1]]
travelled=0
while True:
    for pos in todo:
        char = m[pos[1],pos[0]]
        x,y = pos
        if (char in connections) and (pos in g.nodes):
            for u,v in connection[char]:
                # print(pos,(x,y),(u,v),m[y+v,x+u])
                if (x+u,y+v) not in g.nodes:
                    todo.append((x+u,y+v))
                    travelled+=1
                g.add_edge((x,y),(x+u,y+v))
                g.add_node((x,y))
                g.add_node((x+u,y+v))

        todo.remove(pos)
    if len(todo)==0:
        break

print(travelled//2)
exit()
print(len(g.nodes))

print(g.nodes)

all_lengths= []
# try from outside in?
# exit()
paths = [] 
for n in tqdm.tqdm(g.nodes):
    try:
        pl = nx.shortest_path_length(g,spos[::-1],n)
        all_lengths.append((n,pl))
        paths.append(pl)
    except nx.exception.NetworkXNoPath:
        pass
    # print(pl,max(all_lengths))

if file=='input10.txt':
    debug = False
else:
    debug = True 

o = np.zeros_like(m,dtype=int)

for ans in all_lengths:
    try:
        o[ans[0][::-1]] = ans[1]
    except IndexError:
        pass
if debug:
    print(m)
    print(o)
print(max(all_lengths, key=lambda x:x[1]))
print('part1:',max(paths),travelled//2)

# enclosed 

from skimage.morphology import flood_fill
# if you pad it out, then you always fill out the non enclosed bits.
n = flood_fill(np.pad(o,1),seed_point=(0,0),new_value=-1)
# print(n)
print(len(np.where(n==0)[0]))
# for x in nx.connected_components(g):
#     print(x)