import math
t = input()

for case_t in xrange(t):
    n, m, k = map(int, raw_input().split())
    ans = 0
    if n < m:
        n, m = m, n

    if n - k < 1 or m - k < 1:
        ans = -1
    elif (n - (2*k)) < 3:
        ans = -1
    else:
        # .x...
        # ...x.
        ans = math.ceil(m/(k*1.0))

    ub = 5 if k == 1 else 4
    ans = int(min(ans, ub))
    output = 'Case #' + str(case_t+1) + ': ' + str(ans)
    print output
