import sys

def solve(m, c, coins):
    cache = [0]*(m+1)

    for i, v in enumerate(coins):
        if v > m:
            break
        cache[v] += 1
        for j in xrange(coins[0],m-v+1):
            if cache[j] > 0:
                cache[j+v] += cache[j]
    return cache[m]

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline().rstrip(' \t\r\n\0')
    for _ in xrange(int(rl())):
        m, c = map(int, rl().split())
        coins = sorted(map(int, rl().split()))
        print solve(m, c, coins) % 1000000007
