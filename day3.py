lines = open('input3.txt','r').read().split('\n')[:-1]
# lines = open('input3_example.txt','r').read().split('\n')[:-1]

print(lines)

def check(x,y):
    whitelist = '1234567890.'
    for d in [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]:
        try:
            if lines[y+d[1]][x+d[0]] not in whitelist:
                return True
        except IndexError:
            pass
    return False

def neargear(x,y,location=False):
    for d in [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]:
        try:
            if lines[y+d[1]][x+d[0]] =='*':
                if location:
                    return (x+d[0],y+d[1])
                else:
                    return True
        except IndexError:
            pass
    return False



total = 0 
value=''
next_to=False

for y,line in enumerate(lines):
    # check digit here. 
    if (len(value)>0) and next_to:
        total+=int(value)
    next_to=False
    value=''

    for x,char in enumerate(line):
        if char.isdigit():
            value+=char
            if check(x,y):
                next_to = True
        else:
            if (len(value)>0) and next_to:
                total+=int(value)

            next_to=False    
            value=''

print(total)   


from collections import defaultdict

gears = defaultdict(list)
# part 2 
# find all * chars, and their number pairs. 

value =''
next_to_gear =False
for y,line in enumerate(lines):
    if (len(value)>0) and near_to_gear:
        gears[g_loc].append(int(value))

    near_to_gear=False
    value=''

    for x,char in enumerate(line):
        if char.isdigit():
            value+=char
            
            if neargear(x,y):
                # print(char)
                near_to_gear=True  
                g_loc= neargear(x,y,location=True)
        else:
            if (len(value)>0) and (near_to_gear==True):
                gears[g_loc].append(int(value))

            near_to_gear=False    
            value=''

# times all the gear pairs 
part2 = 0
for k,v in gears.items():
    # print(v)
    if len(v)==2:
        print(v)
        part2+=v[0]*v[1]

print(part2)
# too low 
# 85010461