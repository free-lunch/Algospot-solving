import sys


graph = None
def count_couples(n, visited):
    # Visit all friends
    if visited == (1<<n)-1:
        return 1

    ret = 0
    start = -1
    # Select next seed
    for i in xrange(n):
        if not (visited & (1<<i)):
            start = i
            break

    # Recursive call this function with couple(start, not visited friend)
    for i in xrange(start+1, n):
        if not (visited & (1<<i)):
            if graph[start][i]:
                ret += count_couples(n, visited+(1<<start)+(1<<i))

    return ret

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline().rstrip(' \t\r\n\0')
    for _ in xrange(int(rl())):
        n, m = map(int, rl().split())
        graph = [[False]*n for _ in xrange(n)]
        friends = map(int, rl().split())
        for i in xrange(0,m*2,2):
            graph[friends[i]][friends[i+1]] = True
            graph[friends[i+1]][friends[i]] = True
        print count_couples(n, 0)
