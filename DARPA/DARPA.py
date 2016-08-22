import sys

diffs = None
N, M = None, None

def decision(minimum):
    cosum = 0
    cnt = 0
    for i in xrange(M-1):
        cosum += diffs[i]
        if cosum >= minimum:
            cosum = 0
            cnt += 1
            if cnt == N-1:
                return True
    return False

def solve():
    lo = 0.0
    hi = 240.0
    mid = (lo+hi)/2
    while hi-lo > 0.009:
        if decision(mid):
            lo = mid
        else:
            hi = mid
        mid = (lo+hi)/2

    return mid


if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()
    for _ in xrange(int(rl())):
        N, M = map(int, rl().split())
        locations = map(float, rl().split())
        diffs = [-1]*(M-1)
        for i in xrange(len(locations)-1):
            diffs[i] = locations[i+1] - locations[i]
        print "{:.2f}".format(round(solve(), 2))
