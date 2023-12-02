import copy
f = open('input1.txt','r')
lines = f.read().split('\n')[:-1]

# lines = ['two1nine',
# 'eightwothree',
# 'abcone2threexyz',
# 'xtwone3four',
# '4nineeightseven2',
# 'zoneight234',
# '7pqrstsixteen']
# lines=['zfourvxngsmmqsldpkrrbfnjf2mvkdhfs7eightwotc']
total=0
numberwords = {'one':'1', 'two':'2', 'three':"3", 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
for line in lines:
    nums = []
    #replace it with digits. but need to do it in character order.

    buffer = ''
    for c in line:
        if c.isdigit():
            nums.append(c)
        else:
            buffer+=c

        for k,v in numberwords.items():
            if k in buffer:
                nums.append(v)
                loc = buffer.index(k)
                buffer=buffer[loc+2:]
                # print(buffer)
                
    print(line,int(nums[0]+nums[-1]),nums)
    total+=int(nums[0]+nums[-1])

# print(line)
print(total)