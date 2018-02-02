import time

start = time.time()
def count_zom_in_sq(x, y, r, zombies):
    insq = []

    for zom in zombies:
        zx, zy = zom
        if x <= zx <= (x+r) and y <= zy <= (y+r):
            insq.append(zom)
    return insq

def count_zom_2sq(zoms1, zoms2):
    return len(set(zoms1) | set(zoms2))

t = input()

for case_t in xrange(t):
    num_zombies, r = map(int, raw_input().split())

    zombies = [0] * num_zombies
    for z in xrange(num_zombies):
        x, y = map(int, raw_input().split())
        zombies[z] = (x, y)

    godset = set()
    for x in xrange(len(zombies)):
        for y in xrange(len(zombies)):
            godset.add((zombies[x][0], zombies[y][1]))

    maxpos = 0
    for xy in godset:
        for xy2 in godset:
            x, y = xy
            x2, y2 = xy2
            sq1zom = count_zom_in_sq(x, y, r, zombies)
            sq2zom = count_zom_in_sq(x2, y2, r, zombies)
            maxpos = max(maxpos, count_zom_2sq(sq1zom, sq2zom))

    output = 'Case #' + str(case_t+1) + ': ' + str(maxpos)
    print output

#
#                    _oo0oo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                   0\  =  /0
#                 ___/`---'\___
#               .' \\|     |// '.
#              / \\|||  :  |||// \
#             / _||||| -:- |||||- \
#            |   | \\\  -  /// |   |
#            | \_|  ''\---/''  |_/ |
#            \  .-\__  '-'  ___/-. /
#          ___'. .'  /--.--\  `. .'___
#       ."" '<  `.___\_<|>_/___.' >' "".
#      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#      \  \ `_.   \_ __\ /__ _/   .-` /  /
#  =====`-.____`.___ \_____/___.-`___.-'=====
#                    `=---='
#
#
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
