import sys
from math import factorial

num_combination = lambda n, m: factorial(n) / factorial(abs(n-m)) / factorial(m)
def get_order(N,M,K):
    cosum = 1
    zero_select = 1
    for i in xrange(M, N+M):
        calc = num_combination(i, zero_select)
        zero_select += 1
        if cosum + calc >= K:
            return K-cosum, i

        cosum += calc
    return None

def solve(N,M,K):
    if N == 0 and M == 0:
        return  "NONE"

    if N == 0 or M == 0:
        if K == 1:
            return "a"*N+"b"*M
        else:
            return "NONE"

    if num_combination(N+M,M) < K:
        return "NONE"

    n, m, k = N, M, K
    orders = [0]

    if k == 1:
        for i in xrange(M):
            orders.append(i)

    while k > 1 and n > 0 and m > 0 :
        # Get start point of 1 and remain k
        order = get_order(n,m,k)
        orders.append(order[1])
        k = order[0]
        n -= order[1] - orders[-1]
        m -= 1

        if k == 1 and m > 0:
            for i in xrange(m):
                orders.append(i)

    ret = ["a"]*(N+M)
    for i in orders[1:]:
        ret[-i-1] = "b"

    return "".join(ret)

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()

    for _ in xrange(int(rl())):
        N, M, K = map(int, rl().split())
        print solve(N, M, K)
