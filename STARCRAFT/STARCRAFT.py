import sys
from math import factorial

def solve(p, k):
    combination = lambda n, k: factorial(n) / (factorial(n-k)*factorial(k))
    p = 1.0*p/100
    all_win = p**k

    ret = all_win
    for i in xrange(1,k):
        ret += combination(k+(i-1),i) *  (1.0 - p)**i * all_win

    return ret

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()
    for _ in xrange(int(rl())):
        p, k = map(int, rl().split())
        print(int(round(solve(p, k)*100)))
