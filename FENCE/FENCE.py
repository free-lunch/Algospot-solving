import sys

def solve(fences):
    stack = []
    ret = 0
    # stack = [(idx, value)]
    for cur, v in enumerate(fences):
        new_idx = cur
        while stack and stack[-1][1] >= v:
            ret = max(ret, stack[-1][1] * (cur - stack[-1][0]))
            new_idx = stack.pop()[0]
        stack.append((new_idx, v))

    return ret

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline().rstrip(' \t\r\n\0')
    for _ in xrange(int(rl())):
        n = int(rl())
        fences = map(int, rl().split())
        fences.append(0)
        print solve(fences)
