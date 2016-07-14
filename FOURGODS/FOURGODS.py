import sys
from collections import defaultdict

def solve(v, e, graph):
    ret = 0
    for start in xrange(v):
        paths = [[0]*v for i in xrange(3)]
        paths[0][start] = 1
        for i in xrange(1,3):
            for j in xrange(v):
                if paths[i-1][j] != 0:
                    for k in xrange(v):
                        if graph[j][k]:
                            paths[i][k] += paths[i-1][j]

        for i in xrange(start+1, v):
            if paths[2][i] > 1:
                # Select 2nd, 4th points and then divide 2 because of non-order
                ret += paths[2][i]*(paths[2][i]-1)/2

    # Divide 2 because 1st, 3rd points are non-order
    return (ret/2) % 20130728

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()
    for _ in xrange(int(rl())):
        v, e = map(int, rl().split())
        graph = [[False]*v for _ in xrange(v)]
        for _ in xrange(e):
            v1, v2 = map(int, rl().split())
            graph[v1-1][v2-1] = True
            graph[v2-1][v1-1] = True

        print solve(v, e, graph)
