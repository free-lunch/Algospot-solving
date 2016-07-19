import sys
from heapq import *

def solve(l):
    ret = 0
    q = sorted(l)
    
    while len(q) > 1:
        a = heappop(q)
        b = heappop(q)
        ret += a+b
        heappush(q,a+b)

    return ret


if __name__ == "__main__":
    rl = lambda : sys.stdin.readline().rstrip(' \t\r\n\0')
    for _ in xrange(int(rl())):
        rl()
        str_list = map(int, rl().split())
        print solve(str_list)
