import sys
import collections

def get(state, index):
    return (state >> (index * 2)) & 3

def set(state, index, value):
    return (state & ~(3<< (index * 2))) | (value << (index * 2))

def inc(n):
    if n > 0 :
        return n + 1
    elif n < 0:
        return n - 1
    else:
        return 0

def set_list(state, index_list, value):
    ret = state
    for i in index_list:
        ret = set(ret, i, value)
    return ret

d = dict()
def precalc(disk_num):
    print 'hello'
    end = 0
    for i in xrange(1,disk_num+1):
        end = set(end, i, 3)

    d[end] = 0

    q = collections.deque()
    q.append(end)

    while q :
        parent = q.popleft()
        top = [-1,-1,-1,-1]
        for n in xrange(disk_num+1,0,-1):
            top[get(parent, n)] = n

        for i in xrange(4):
            if top[i] != -1:
                for j in xrange(4):
                    if i != j and (top[j] == -1 or top[j] > top[i]):
                        child = set(parent, top[i], j)
                        if not child in d:
                            d[child] = d[parent] + 1
                            q.append(child)


def solve(disk_num, state):
    end = 0
    for i in xrange(1,disk_num+1):
        end = set(end, i, 3)

    if end == state:
        return 0

    c = dict()

    c[end] = -1
    c[state] = 1

    q = collections.deque()
    q.append(state)
    q.append(end)

    while q :
        parent = q.popleft()
        top = [-1,-1,-1,-1]
        for n in xrange(disk_num+1,0,-1):
            top[get(parent, n)] = n

        for i in xrange(4):
            if top[i] != -1:
                for j in xrange(4):
                    if i != j and (top[j] == -1 or top[j] > top[i]):
                        child = set(parent, top[i], j)
                        if not child in c:
                            c[child] = inc(c[parent])
                            q.append(child)
                        else:
                            if c[child] * c[parent] < 0:
                                return abs(c[child]) + abs(c[parent]) -1
    return -1



if __name__ == "__main__":
    rl = lambda : sys.stdin.readline().rstrip('\n')
    for _ in xrange(int(rl())):
        disk_num = int(rl())
        state = 0
        for i in xrange(4):
            state = set_list(state, map(int, rl().split()[1:]), i)
        print solve(disk_num, state)

    # For random test
    # import random
    # n = 10
    #
    # for _ in xrange(2):
    #     state = 0
    #     for i in xrange(1,n+1):
    #         state = set(state,i,random.randrange(0,4))
    #     print solve(n, state)
