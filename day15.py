def hasher(s):
    total = 0
    for c in s:
        total += ord(c)
        total *= 17
        total = total%256        
    return total

assert 52 == hasher('HASH')
lines = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'.split(',')
lines = open('input15.txt','r').read()[:-1].split(',')
# print(open('input15.txt','r').read()[:-1])
t = 0
for lin in lines:
    # print(lin)
    t+=hasher(lin)
print(t)
#514019 wrong?!
from collections import defaultdict,OrderedDict
m=defaultdict(OrderedDict)
lines = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'.split(',')
lines = open('input15.txt','r').read()[:-1].split(',')
pos = 0
for line in lines:
    print(line)
    if '-' in line:
        # remove a lens
        label = line.split('-')
        for k,v in m.items():
            if label[0] in v.keys():
                v.__delitem__(label[0])

    elif '=' in line:
        label = line.split('=')
        pos = hasher(label[0])
        m[pos][label[0]] = int(label[1])

# calc power
total = 0 
for k,v in m.items():
    for i,j in enumerate(v.values()):
        total+=(1+k)*(i+1)*j
        # print(i,j,k)
print(total)