import networkx as nx
import numpy as np
import tqdm
file= '10.txt'
file = 'input10.txt'
file = '10simple.txt'
m= np.genfromtxt(file,delimiter=1, dtype=str)
print(m)
g = nx.Graph()
connections = 'S|-LJ7F'
connection = {'|':[(0,-1),(0,1)],'-':[(-1,0),(1,0)],'L':[(0,-1),(1,0)],'J':[(0,-1),(-1,0)],'7':[(0,1),(-1,0)],'F':[(0,1),(1,0)]}
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

connection['S'] = connection[Spipe]

for y,row in enumerate(m):
    for x,pos in enumerate(row):
        if pos in connections:

            for u,v in connection[pos]:
                g.add_edge((x,y),(x+u,y+v))
                g.add_node((x,y))
                g.add_node((x+u,y+v))

print(len(g.nodes))

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

if debug:
    o = np.zeros_like(m,dtype=int)
    for ans in all_lengths:
        o[ans[0][::-1]] = ans[1]
    print(m)
    print(o)
print(max(all_lengths, key=lambda x:x[1]))
print(max(paths))

# enclosed 

from skimage.morphology import flood_fill

n = flood_fill(o,seed_point=(0,0),new_value=-1)
print(n)
print(len(np.where(n==0)[0]))
# for x in nx.connected_components(g):
#     print(x)