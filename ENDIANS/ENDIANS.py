import sys

def trans_order(n):
    x, y = divmod(n, 8)
    ret = 31 - (8*x)
    ret += -7 + y

    return ret

def solve(n):
    ret = 0
    for i in xrange(32):
        if n & (1<<i):
            ret += (1 << trans_order(i))
    return ret

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline().rstrip(' \t\r\n\0')
    for _ in xrange(int(rl())):
        print solve(int(rl()))
