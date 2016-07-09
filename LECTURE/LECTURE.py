import sys
import re
if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()
    for _ in xrange(int(rl())):
        print "".join(sorted(re.findall('..', rl())))
