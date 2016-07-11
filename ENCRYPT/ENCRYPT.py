import sys

rl = lambda:sys.stdin.readline().rstrip().rstrip(' \t\r\n\0')
for _ in xrange(int(rl())):
    s = rl()
    print(s[::2]+s[1::2])
