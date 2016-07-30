import sys

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline().rstrip(' \t\r\n\0')
    for _ in xrange(int(rl())):
        rl()
        ret = 0
        input = map(int, rl().split())
        for i in xrange(len(input)):
            if (i+1) == input[i]:
                ret += 1

        print ret
