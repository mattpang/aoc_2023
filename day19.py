# px: [cond :[cond:[a,b],c]]
# qqz = {s>2770: T: Qs, F: {m>1801 , T: hdj F:R }}
from collections import namedtuple


lines = '''px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}'''.splitlines()

lines= open('input19.txt','r').read().splitlines()
rules = dict()

for pidx,line in enumerate(lines):
    if line =='':
        break
    print(line)
    r, cond = line[:-1].split('{')
    rules[r] = cond
    

# always start at 'in'

def travel(rule, p):
    conds = rule
    logic = conds.split(',')
    x = p.x
    m = p.m
    a = p.a
    s = p.s
    for rule in logic:
        cond = rule.split(':')[0]
        if cond=='A':
            return 1
        elif cond=='R':
            return 0
        elif ('>' not in cond) and ('<' not in cond):
            return travel(rules[cond],p)
        else:
            if eval(cond):
                # send to next thing.
                next_rule = rule.split(':')[1].split(',')[0]
                # print(next_rule,next_rule=='A')
                if next_rule=='A':
                    return 1
                elif next_rule=='R':
                    return 0
                elif ('>' not in next_rule) and ('<' not in next_rule):
                    return travel(rules[next_rule],p)

Part = namedtuple('Part', ['x','m','a','s'])

score = 0
for line in lines[pidx+1:]:
    print(line[1:-1])
    x,m,a,s = [int(m.split('=')[1]) for m in line[1:-1].split(',')]
    p = Part(x,m,a,s)

    result = travel(rules['in'],p)
    if result==1:
        score += p.x+p.m+p.a+p.s
print(score)