import networkx as nx 
lines = open('./input25.txt','r').read().splitlines()
g = nx.Graph()

for line in lines:
    a,b = line.split(': ')
    c = b.split(' ')
    for e in c:
        g.add_edge(a.strip(),e.strip())

components=list(nx.connected_components(g))
cuts = nx.minimum_edge_cut(g)

for a,b in cuts:
    g.remove_edge(a,b)

t = 1 
for s in nx.connected.connected_components(g):
    print(len(s))
    t*=len(s)
print(t)

