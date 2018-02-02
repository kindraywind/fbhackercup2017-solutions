import operator as op
import math

def ncr(n, r):
    r = min(r, n-r)
    if r == 0:
        return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom


def probofdice(p, n, s):
    # prob to get sum of p when rolling n dices with s-faces die.
    prob = 0
    try:
        kmax = int(math.floor((p - n) / (s*1.0)))
        modi = (1.0 / s**n)
        sum = 0
        for k in range(kmax+1):
            sum += (-1)**k * ncr(n, k) * ncr(p-(s*k)-1, p-(s*k)-n)

        prob = modi * sum
    except:
        prob = 0
    return prob

def proprange(p, pend, n, s):
    sum = 0
    for i in xrange(p, pend+1):
        sum += probofdice(i, n, s)

    return sum

def parsespell(spell):
    s = [spell]

    if '+' not in spell and '-' not in spell:
        z = 0
    elif '+' in spell:
        s = spell.split('+')
        z = int(s[1])
    elif '-' in spell:
        s = spell.split('-')
        z = -1 * int(s[1])
    s1 = s[0].split('d')
    times = int(s1[0])
    face = int(s1[1])
    return (times, face, z)

def maxkillprob(zhp, spells):
    maxprob = 0
    for spell in spells:
        times, face, z = parsespell(spell)
        maxpos = face * times
        prob = proprange(zhp-z, maxpos, times, face)
        maxprob = max([maxprob, prob])
    return maxprob


numzombies = input()

for i in range(numzombies):
    hp, nspell = map(int, raw_input().split())
    spells = raw_input().split()
    output = 'Case #' + str(i+1) + ': ' + format(maxkillprob(hp, spells), '.6f')
    print output
