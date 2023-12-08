from itertools import product
race = [[7,9],[15,40],[30,200]]
race = [[52,426],[94,1374],[75,1279],[94,1216]]
race = [[52947594,426137412791216]]
# race = [[71530,940200]]
# hold down for n seconds, to gain v speed per second.
# still need to get to d distance away within t time. 
# t = 7
def part1(race):
    winners = 1
    t = 7 
    d = 9 
    for t,d in race:
        # how many ways to win?
        wins = 0 
        for i in range(1,t+1):
            # print(t,i,(t-i)*i)
            if (t-i)*i>d:
                wins+=1
        print(wins)
        winners*=wins
        # break
    print(winners)

# 7-2 * 2
def part2(race):
    t,d = race[0]
    # basically how many are there?
    # i*(t-i) >d 
    # i*t-i**2 > d 
    # lowest + highest
    # lowest when i is 1
    # lowest = d//t+1
    #
    import numpy  as np
    lowest = 0.5*(t-np.sqrt(t**2-4*d))
    highest = 0.5*(t+np.sqrt(t**2-4*d))

    print(int(highest-lowest))

part2(race)