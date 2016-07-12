import sys

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()
    d = []
    for _ in xrange(int(rl())):
        input = rl().split()
        n, str = int(input[0]), input[1]
        d.append(str[:n-1]+str[n:])

    for i, v in enumerate(d):
        print i+1, v
