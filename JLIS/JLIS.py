import sys

cache = [[-1] * 101 for _ in xrange(101)]

def get_max_item(i, j):
    if i is -1:
        a = -sys.maxint
    else:
        a = A[i]
    if j is -1:
        b = -sys.maxint
    else:
        b = B[j]
    return max(a, b)


def jlis(i, j):
    if cache[i+1][j+1] != -1:
        return cache[i+1][j+1]

    max_item = get_max_item(i, j)
    ret = 2
    for next_i in xrange(i+1, len(A)):
        if max_item < A[next_i]:
            ret = max(ret, jlis(next_i, j)+1)

    for next_j in xrange(j+1, len(B)):
        if max_item < B[next_j]:
            ret = max(ret, jlis(i, next_j)+1)

    cache[i+1][j+1] = ret
    return ret


if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()
    global A, B
    for _ in xrange(int(rl())):
        rl()
        A = map(int, rl().split())
        B = map(int, rl().split())
        cache = [[-1]*(len(B)+1) for _ in xrange(len(A)+1)]
        print(jlis(-1, -1)-2)
