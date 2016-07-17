import sys
from math import factorial


def solve(n):
    combination = lambda n, r : factorial(n)/factorial(n-r)/factorial(r)
    x, y = divmod(n,2)
    ret = 0
    for i in xrange(x+1):
        ret += combination(n-i,i)
    return ret

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline().rstrip(' \t\r\n\0')
    for _ in xrange(int(rl())):
        n = int(rl())
        print solve(n) % 1000000007
