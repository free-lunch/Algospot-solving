import sys

rl = lambda : sys.stdin.readline().rstrip(' \t\r\n\0')

for _ in xrange(int(rl())):
    print "Hello, {0}!".format(rl())
