import sys

def decision(str):
    n = len(str)
    if [str[0]]*n == str:
        return 1

    diff = str[0] - str[1]
    progressive = True
    for i in xrange(n-1):
        if diff != str[i] - str[i+1]:
            progressive = False
            break

    if progressive:
        if abs(diff) == 1:
            return 2
        else:
            return 5

    for i in xrange(n):
        if str[i] != str[i%2]:
            return 10

    return 4


def solve(PI):
    n = len(PI)
    cache = [sys.maxint] * (n)
    cache[2] = decision(PI[0:3])
    cache[3] = decision(PI[0:4])
    cache[4] = decision(PI[0:5])

    for i in xrange(3,n):
        try:
            for j in xrange(3,6):
                if i-j >= 0:
                    cache[i] = min(decision(PI[i-j+1:i+1]) + cache[i-j], cache[i])
        except:
            continue
    print cache[-1]

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline().rstrip(' \t\r\n\0')

    for _ in xrange(int(rl())):
        solve(map(int,list(rl())))
