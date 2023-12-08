import networkx as nx
from itertools import cycle

lines = open('input8.txt','r').read().splitlines()
# lines = open('8b.txt','r').read().splitlines()

steps = lines[0]
edges = dict()
first = None
for line in lines[2:]: 
    start_node = line.split(' =')[0]
    l,r = line[:-1].split('(')[1].split(', ')
    edges[start_node] = [l,r]

# travseral
def part1(start = 'AAA',end = 'ZZZ'):
    taken=1
    s = cycle(steps)
    taken = 1
    for i in s:
        print(i)
        if i=='L':
            start = edges[start][0]
        else:
            start = edges[start][1]

        if start == 'ZZZ':
            print(taken)
            return taken
            break

        taken+=1

part1()


def part2(start = 'AAA',end = 'ZZZ'):
    taken=1
    s = cycle(steps)
    taken = 1
    for i in s:
        print(i)
        if i=='L':
            start = edges[start][0]
        else:
            start = edges[start][1]

        if start[2] == 'Z':
            print(taken)
            return taken
            break

        taken+=1

# exit()
# part 2
s = cycle(steps)
#all nodes that end with A
starts = sorted([x for x in edges.keys() if x[2]=='A'])
print(starts)
ends = sorted([x for x in edges.keys() if x[2]=='Z'])
print(ends)

taken_list = []

for start in starts:
    taken_list.append(part2(start))

print(taken_list)
import math 
print(math.lcm(*taken_list))