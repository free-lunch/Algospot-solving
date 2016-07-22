import sys

cache = None
def precalc():
    global cache
    cache = [[0]*i for i in xrange(1,1002)]
    cache[1][0] = 0.75
    cache[1][1] = 0.25
    for i in xrange(1000):
        for j in xrange(i+1):
            cache[i+1][j] += cache[i][j]*0.75
        for j in xrange(i+1):
            cache[i+1][j+1] += cache[i][j]*0.25

def solve(n, m):
    ret = 0
    for i in xrange(2*m-n+1):
        ret += cache[m][i]
    return ret

if __name__ == "__main__":
    precalc()
    rl = lambda: sys.stdin.readline()
    for _ in xrange(int(rl())):
        n, m = map(int, rl().split())
        print "{:.10f}".format(solve(n, m))
