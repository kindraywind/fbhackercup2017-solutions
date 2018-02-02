import math

def maxtrip(items):
    heaviest = items[0]

    count = 0
    while int(math.ceil(50.0 / items[0])) <= len(items):
        # print 'len', len(items), 'need', 50.0 / heaviest, heaviest
        count += 1
        heaviest = items.pop(0)
        itemsneeded = int(math.ceil(50.0 / heaviest))
        itemsneeded -= 1
        items = items[0:len(items)-itemsneeded]
        if len(items) == 0:
            break

    return count

t = input()

days = [0] * t
for i in range(t):
    itemsno = input()
    days[i] = [0] * itemsno
    for j in range(itemsno):
        days[i][j] = input()
        days[i] = sorted(days[i], key=int, reverse=True)

i = 1
for day in days:
    output = 'Case #' + str(i) + ': ' + str(maxtrip(day))
    print output
    i += 1
