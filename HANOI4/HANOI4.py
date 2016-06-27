import sys
import collections

# Move i -> j

def move2tuple(tup, i, j):
    l = list(tup)
    l[j] = tup[j] + (tup[i][-1],)
    l[i] = tup[i][:len(tup[i])-1]
    return tuple(l)

def inc(n):
    if n > 0 :
        return n + 1
    elif n < 0:
        return n - 1
    else:
        return 0

def solve(disk_num, state):
    end = (),(),(),tuple([i for i in xrange(disk_num,0,-1 )])
    if end == state:
        return 0

    c = dict()
    c[end] = -1
    c[state] = 1

    q = collections.deque()
    q.append(state)

    while q :
        parent = q.popleft()
        for i in xrange(4):
            if parent[i]:
                for j in xrange(4):
                    if i != j and (not parent[j] or parent[j][-1] > parent[i][-1]):
                        child = move2tuple(parent, i, j)
                        if not child in c:
                            c[child] = inc(c[parent])
                            q.append(child)
                        else:
                            if c[child] * c[parent] < 0:
                                return abs(c[child]) + abs(c[parent]) -1

    return c[end]


if __name__ == "__main__":
    rl = lambda : sys.stdin.readline().rstrip('\n')
    for _ in xrange(int(rl())):
        disk_num = int(rl())
        state = ()
        for i in xrange(4):
            state += tuple(map(int, rl().split())[1:]),

        print solve(disk_num, state)
