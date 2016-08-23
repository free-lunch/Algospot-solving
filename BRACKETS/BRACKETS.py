import sys

d = {'[': ']', '(':')'}
cache = [[-1]*101 for _ in xrange(101)]
brackets = None

def solve(start, end):
    if start >= end:
        return 0

    if cache[start][end] != -1:
        return cache[start][end]

    ret = 0
    if brackets[start] == "(" or brackets[start] == "[":
        s_point = start+1
        while True:
            try :
                next_index = brackets.index(d[brackets[start]], s_point, end+1)
            except :
                break

            ret_sub = 2 + solve(start+1, next_index-1) + solve(next_index+1, end)
            ret = max(ret, ret_sub)
            s_point = next_index+1

        ret = max(ret, solve(start+1, end))
    else:
        ret = solve(start+1, end)

    cache[start][end] = ret
    return ret

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()
    while True:
        brackets = rl().rstrip()

        if brackets == "end":
            break

        for i in xrange(len(brackets)):
            for j in xrange(len(brackets)):
                cache[i][j] = -1

        print solve(0, len(brackets)-1)
