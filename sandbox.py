hardmap =\
["xxxxxxxxxxxxxxxxxxxxxxxxxx",
 "xs..........ff.x.....x.x.x",
 "xxxx..xx..xxx..x..x..x.x.x",
 "xd.........x.f....x....x.x",
 "x..xxx.....x..xxxxx...xx.x",
 "x..x...................x.x",
 "x..x.xxxxxxfx..x.....xxx.x",
 "x....xr.....x..xxxx..xdx.x",
 "xxx..x......x..xd....xxx.x",
 "x....xxxxxfxx..x..x....x.x",
 "xFWPN....x........x..f.x.x",
 "x............x.fxxxx...x.x",
 "xx...xxxxx...f.....x...x.x",
 "x.....x......xxxx..w.f.x.x",
 "x..xxxx...xxxx.rx...x..xwx",
 "x.......w....x..x...x..xfx",
 "xxxxxxx..x...x..x..xx..xwx",
 "xd...w...x...x...f.....xfx",
 "xxxxxxxxxxxxxxxxxxxxxxxxxx"]

hardmap2 =\
["xxxxxxxxxxxxxxxxxxxxxxxxxx",
 "xs....f........x.....x.x.x",
 "xxxx..xx..xxx..x..x..x.x.x",
 "x..........x......x....x.x",
 "x..xxx.....x..xxxxx...xx.x",
 "x..x...................x.x",
 "x..x.xxxxxx.x..x.....xxx.x",
 "x....xr.....x..xxxx..xdx.x",
 "xxx..x......x..xd....xxx.x",
 "x....xxxxx.xx..x..x....x.x",
 "x........x........x....x.x",
 "x............x..xxxx...x.x",
 "xx...xxxxx.........x...x.x",
 "x.....x......xxxx......x.x",
 "x..xxxx...xxxx.rx...x..x.x",
 "x............x..x...x..x.x",
 "xxxxxxx..x...x..x..xx..x.x",
 "xd.......x...x.........x.x",
 "xxxxxxxxxxxxxxxxxxxxxxxxxx"]


currstack = []

def getstack(map):
    count = 17
    stack = []
    while count > 0:
        stack.append(map[count][24])
        count = count - 1
    return stack

def stackmodify(stack, action):
    if action == 'F':
        count = 0
        loop = True
        while count < 17 and loop:
            if stack[count] == '.':
                stack[count] = 'f'
                loop = False
            else:
                count = count + 1
    if action == 'W':
        count = 0
        loop = True
        while count < 17 and loop:
            if stack[count] == '.':
                stack[count] = 'w'
                loop = False
            else:
                count = count + 1
    if action == 'P':
        count = 16
        loop = True
        while count >= 0 and loop:
            if stack[count] != '.':
                stack[count] = '.'
                loop = False
            else:
                count = count -1
    return stack

def mapmodify(stack, action, map1 = hardmap):
    if action == 'start':
        map1 = startmap
    if action == 'final':
        map1 = finalmap
    else:
        map1 = ["xxxxxxxxxxxxxxxxxxxxxxxxxx",
            "xxxxxxx..x...x..x..xx..x" + stack[16] + "x",
            "xxxxxxx..x...x..x..xx..x" + stack[15] + "x",
            "xd.......x...x.........x" + stack[14] + "x",
            "xxxxxxx..x...x..x..xx..x" + stack[13] + "x",
            "xd.......x...x.........x" + stack[12] + "x",
            "xxxxxxx..x...x..x..xx..x" + stack[11] + "x",
            "xd.......x...x.........x" + stack[10] + "x",
            "xxxxxxx..x...x..x..xx..x" + stack[9] + "x",
            "xd.......x...x.........x" + stack[8] + "x",
            "xxxxxxx..x...x..x..xx..x" + stack[7] + "x",
            "xd.......x...x.........x" + stack[6] + "x",
            "xxxxxxx..x...x..x..xx..x" + stack[5] + "x",
            "xd.......x...x.........x" + stack[4] + "x",
            "xxxxxxx..x...x..x..xx..x" + stack[3] + "x",
            "xd.......x...x.........x" + stack[2] + "x",
            "xxxxxxx..x...x..x..xx..x" + stack[1] + "x",
            "xd.......x...x.........x" + stack[0] + "x",
            "xxxxxxxxxxxxxxxxxxxxxxxxxx"]
    return map1

            
'''            
print currstack
currstack = getstack(hardmap)
print currstack
currstack = stackmodify(currstack, 'F')
print currstack
hardmap = mapmodify(currstack, 'f')
print hardmap
'''

