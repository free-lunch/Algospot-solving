import sys

week_day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',\
            'Thursday', 'Friday', 'Saturday']
number_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline().rstrip(' \t\r\n\0')
    for _ in xrange(int(rl())):
        m, d, s = rl().split()
        m = int(m)-1
        d = int(d)
        s = week_day.index(s)

        start = d - s
        ret = ["",]*7

        for i in xrange(7):
            # Count a day of previous month
            if start + i < 1:
                if m == 1:
                    ret[i] = str(start + i + number_day[11])
                else:
                    ret[i] = str(start + i + number_day[m-1])
            # Count a day of next month
            elif start + i > number_day[m]:
                ret[i] = str(start + i - number_day[m])
            else:
                ret[i] = str(start + i)

        print ' '.join(ret)
