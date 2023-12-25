lines = '''jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr'''.splitlines()
lines = open('./input25.txt','r').read().splitlines()
import networkx as nx 
g = nx.Graph()

for line in lines:
    a,b = line.split(': ')
    c = b.split(' ')
    for e in c:
        g.add_edge(a.strip(),e.strip())

print(g.edges)
h = nx.subgraph(g,['jqt'])

components=list(nx.connected_components(g))
# print(components)
import matplotlib.pyplot as plt 
# nx.draw(g,with_labels=True, font_weight='bold')
# plt.show()
# cut these:
for a,b in [['bmd','ngp'],['tqh','dlv'],['tqr','grd']]:
    print(a,b)
    g.remove_edge(a,b)
# nx.draw(g,with_labels=True, font_weight='bold')
# plt.show()

t = 1 
for s in nx.connected.connected_components(g):
    print(len(s))
    t*=len(s)
print(t)

