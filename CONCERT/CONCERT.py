import sys
N = None
VS = None
VM = None
VN = None
cache = None

def solve():
    cache[0][VS] = 1
    for i in xrange(N):
        for j in xrange(VM+1):
            if cache[i][j] == 1:
                if 0 <= j + VN[i] <= VM:
                    cache[i+1][j+VN[i]] = 1

                if 0 <= j - VN[i] <= VM:
                    cache[i+1][j-VN[i]] = 1

    for i in xrange(VM,-1,-1):
        if cache[N][i] == 1:
            return i

    return -1

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()
    for _ in xrange(int(rl())):
        N, VS, VM = map(int, rl().split())
        VN = map(int, rl().split())
        cache = [[0]*1001 for _ in xrange(51)]

        print solve()
