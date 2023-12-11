import numpy as np
import copy 
g = np.genfromtxt('11.txt',delimiter=1,dtype=str,comments=None)
g = np.genfromtxt('input11.txt',delimiter=1,dtype=str,comments=None)
og = copy.deepcopy(g)
# print(g)
# print(g.shape)
x = 0 
expand_cols=[]
for col in range(g.shape[0]):
    if all(g[col,:] == '.'):
        expand_cols.append(g[col,:])
        x+=1
    
    expand_cols.append(g[col,:])
print(x)
g = np.vstack(expand_cols)
print('expanded rows')
# print(g)
# print(g.shape)
expand_rows = []
for row in range(g.shape[1]):
    if all(g[:,row] == '.'):
        expand_rows.append(g[:,row])
        x+=1
    expand_rows.append(g[:,row])
print(x)
g = np.vstack(expand_rows).T
# print(g)
# get coords of matches

m = np.vstack(np.where(g=='#')).T
print(len(m))
from sklearn.metrics import pairwise_distances
from itertools import combinations

ans = np.tril(pairwise_distances(m,m,metric='manhattan'))
dist = int(ans.sum())
print(dist)

distances = 0
expanded = 0
# count the empty lines in 
m = np.vstack(np.where(og=='#')).T
empty_columns = dict()
for y in range(og.shape[0]):
    empty_columns[y] = int(all(og[y,:]=='.'))
empty_rows = dict()
for x in range(og.shape[1]):
    empty_rows[x] = int(all(og[:,x]=='.'))

for (x1, y1), (x2, y2) in combinations(m, 2):
    expansion = 0
    # need to check if min(g1_y,g2_y):max(g1_y,g2_y) 
    # are in columns that are empty
    for i in range(min(y1,y2),max(y1,y2)):
        expansion+=empty_rows[i]
    for i in range(min(x1,x2),max(x1,x2)):
        expansion+=empty_columns[i]
    expanded += expansion

print(dist+999998*expanded,expanded)

