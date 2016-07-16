import sys

graph = None
cache = None

def dp(n, here, visited):
    if cache[here][visited] >= 0:
        return cache[here][visited]

    cache[here][visited] = sys.maxint
    for nxt in xrange(n):
        if visited & (1<<nxt):
            continue
        if visited + (1<<nxt) == ((1 << n)-1):
            m = graph[here][nxt]
        else:
            m = graph[here][nxt]+ dp(n, nxt, visited + (1<<nxt))
        cache[here][visited] = min(cache[here][visited], m)

    return cache[here][visited]

def solve(n):
    ret = sys.maxint
    for i in xrange(n):
        ret = min(ret, dp(n, i, 1<<i))
    return ret

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()
    for _ in xrange(int(rl())):
        n = int(rl())
        graph = []
        cache = [[-1]*(2**n) for _ in xrange(n)]

        for i in xrange(n):
            input = map(float, rl().split())
            graph.append(input)

        print "{:.10f}".format(solve(n))
