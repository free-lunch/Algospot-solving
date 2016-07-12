import sys

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()
    for _ in xrange(int(rl())):
        x,y = 0,0
        for _ in xrange(3):
            input = map(int, rl().split())
            x ^= input[0]
            y ^= input[1]

        print x, y
