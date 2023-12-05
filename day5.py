from collections import defaultdict

lines = open('./input5.txt').read().split('\n')

# lines = open('./5.txt').read().split('\n')

seeds = list(map(int,lines[0].split(': ')[1].split(' ')))
print(seeds)


lookup = defaultdict(dict)
labels = ['seed']
rules = defaultdict(list)
for line in lines[1:]:
    if '-to-' in line:
        a,b = line.replace(' map:','').split('-to-')
        print(a,b)
        labels.append(b)
    elif len(line)>0:
        s,t,r = map(int,line.split(' '))
        rules[(a,b)].append((s,t,r))
        # for i in range(0,r):
        #     # if a=='seed':
        #     lookup[(a,b)][t+i] = s+i
        #     # else:
        #         # lookup[(a,b)][s+i] = t+i

print(rules)
#     print(line)

# print(labels)
# print(lookup)

# min_loc = 100
# for seed in seeds:
#     pre = seed
#     # print(seed)
#     for a,b in zip(labels,labels[1:]):
#         try:
#             after = lookup[(a,b)][pre]
#         except KeyError:
#             after = pre
#         # print(b,after)
#         pre = after
#         if b=='location' and after<min_loc:
#             min_loc=after

# print(min_loc)

# above is too slow for large range of numbers





print(labels)

def range_check(p,param):
    for a,b,c in rules[param]:
        if b < p <b + c:
            return a + (p-b)
    return p


min_loc = 1E20



for seed in seeds:
    # pre = seed
    # print(seed)
    pre = seed
    for a,b in zip(labels,labels[1:]):
        after = range_check(pre,(a,b))

        if b=='location' and after<min_loc:
            min_loc=after
        pre=after

print(min_loc)


def inverted_checker(p,param):
    for a,b,c in rules[param]:
        if a < p <a + c:
            return b + (p-a)
    return p


def is_needed(n):
    for x, y in zip(seeds[::2], seeds[1::2]):
        if x <= n < x + y:
            return True
    return False


from itertools import count
n=0
labels.reverse()
for n in count(start=40000000):
    i = n 
    for a,b in zip(labels,labels[1:]):
        # print((b,a))
        d = inverted_checker(i,param=(b,a))
        i=d
    
    if is_needed(d):
        print('part2',d-1,n-1)
        break
    
    if n%100000==0:
        print(n)
