import sys

N, W = None, None
items = None
cache = None

def solve(n, capacity):
    if cache[n][capacity] != -1:
        return cache[n][capacity]

    if n == N:
        return 0

    ret = -1
    if capacity >= items[n][1]:
        ret = solve(n+1, capacity - items[n][1]) + items[n][2]

    ret = max(ret, solve(n+1, capacity))
    cache[n][capacity] = ret
    return ret

def reconstruct(n, capa, choose):
    if n == N:
        return

    if solve(n, capa) == solve(n+1, capa) :
        reconstruct(n+1, capa, choose)
    else:
        choose.append(items[n][0])
        reconstruct(n+1, capa-items[n][1],choose)

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()
    for _ in xrange(int(rl())):
        N, W = map(int, rl().split())
        items = [None]*N
        cache = [[-1]*1001 for _ in xrange(101)]
        for j in xrange(N):
            i = rl().split()
            items[j] = [i[0], int(i[1]), int(i[2])]

        needs =  solve(0, W)
        choose = []
        n = 0
        w = W
        for i in xrange(N):
            if cache[i][w] - items[i][2] == cache[i+1][w-items[i][1]]:
                choose.append(items[i][0])
                n += 1
                w -= items[i][1]

        choose = []
        reconstruct(0, W, choose)
        print needs, len(choose)
        for name in choose:
            print name
