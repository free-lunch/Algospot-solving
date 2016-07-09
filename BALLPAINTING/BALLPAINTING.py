import sys

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()
    case = [0]*1001
    case[1] = 2
    for i in xrange(2, 1001):
        case[i] = (case[i-1]*4*(2*i-1)) % 1000000007

    while(True):
        n = int(rl())
        if n == 0:
            break
        print(case[n])
