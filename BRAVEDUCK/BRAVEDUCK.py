import sys
import math
import gc
import collections

def solve(jump, start, end, bridge):
    jump = jump**2
    q = collections.deque()
    q.append(start)

    visited = [False] * len(bridge)

    while q:
        x1, y1 = q.pop()
        for idx, value in enumerate(bridge):
            if visited[idx]:
                continue

            x2 = value[0]
            y2 = value[1]

            if jump >= (end[0]-x1)**2 + (end[1]-y1)**2:
                return 'YES'

            if jump >= (x1-x2)**2 + (y1-y2)**2:
                visited[idx] = True
                q.append((x2,y2))

    return 'NO'

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()

    for _ in xrange(int(rl())):
        jump = int(rl())
        start = map(int, rl().split())
        end = map(int, rl().split())
        bridge = []
        for _ in xrange(int(rl())):
            x,y = map(int, rl().split())
            bridge.append((x,y))

        print solve(jump, start, end, bridge)
