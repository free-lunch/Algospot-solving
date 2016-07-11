import sys

d = dict()
d['kg'] = (2.2046, 'lb')
d['lb'] = (0.4536, 'kg')
d['l'] =  (0.2642, 'g')
d['g'] =  (3.7854, 'l')

if __name__ == "__main__":
    rl = lambda: sys.stdin.readline().rstrip(' \t\r\n\0')
    for i in xrange(int(rl())):
        input = rl().split()
        digits, unit = float(input[0]), input[1]
        print i+1, "{:.4f}".format(round(digits * d[unit][0],4)), d[unit][1]
