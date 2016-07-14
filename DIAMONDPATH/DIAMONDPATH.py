import sys

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()
    for _ in xrange(int(rl())):
        n = int(rl())
        ret = [0]*n
        ret[0] = int(rl())

        for i in xrange(n-1):
            input = map(int, rl().split())
            input[0] += ret[0]
            input[-1] += ret[len(input)-2]
            for j in xrange(1, len(input)-1):
                input[j] += max(ret[j-1],ret[j])
            ret = input

        for i in xrange(n,1,-1):
            input = map(int, rl().split())
            for j in xrange(len(input)):
                input[j] += max(ret[j],ret[j+1])
            ret = input

        print ret[0]
