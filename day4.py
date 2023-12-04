# lines = open('./input4_example.txt').readlines()
lines = open('./input4.txt').readlines()

def make_int(i):
    try:
        return int(i)
    except ValueError:
        pass

total = 0
card_matched = dict()
for i,line in enumerate(lines):
    c, ab =line.split(': ')
    a,b = ab.split('|')

    alist = set(map(make_int,a.strip().split(' ')))
    blist = set(map(make_int,b.strip().split(' ')))
    if None in alist:
        alist.remove(None)
    if None in blist:
        blist.remove(None)

    matches = len(alist.intersection(blist))
    card_matched[i] = matches

    if matches>0:
        score = 2**(matches-1)
    else:
        score = 0
    print(i+1,score)
    total+=score

print(total)
# 37975 too high, too many None in there cocking things up.
# 23441 is correct

# part 2
# for each one line's matches, tally up the rest. 
from collections import defaultdict
import copy 
matched = copy.deepcopy(card_matched)
p2 = 0 
copies = defaultdict(int)
print(copies)
for i in range(len(lines)):
    copies[i]+=1
    for j in range(matched[i]):
        copies[i+1+j] += copies[i]

   
print(sum(copies.values()))
