import Queue as Q

t = input()

for i in xrange(t):
    n, m = map(int, raw_input().split())

    allpie = [0] * n
    piecost = [0] * n
    for day in range(n):
        allpie[day] = map(int, raw_input().split())
        allpie[day].sort()

        p = 1
        piecost[day] = []
        for pie in allpie[day]:
            if p == 1:
                cost = (sum(allpie[day][0:p]) + (p**2))
            else:
                cost = (sum(allpie[day][0:p]) + (p**2)) - ((sum(allpie[day][0:p-1])+(p-1)**2))

            piecost[day].append(cost)
            p += 1

    totalcost = 0
    q = Q.PriorityQueue()
    for pies in piecost:
        for p in pies:
            q.put(p)
        totalcost += q.get()

    output = 'Case #' + str(i+1) + ': ' + str(totalcost)
    print output
