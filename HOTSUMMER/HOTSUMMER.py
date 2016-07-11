import sys

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline().rstrip(' \t\r\n\0')
    for _ in xrange(int(rl())):
        target = int(rl())
        elec_sum = sum(map(int, rl().split()))
        if elec_sum <= target:
            print 'YES'
        else:
            print 'NO'
