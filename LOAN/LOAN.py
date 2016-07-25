import sys

def pay_all_debt(N, M, P, month_pay):
    for i in xrange(M):
        # print N, 1+1.0*P/100
        N *= (1+1.0*P/12/100)
        N -= month_pay
        if N <= 0:
            break
    return N<=0

def solve(N, M, P):
    lo, hi = 0.0, 10.0**8
    while hi -lo > 10**-8:
        mid = (lo+hi)/2
        if pay_all_debt(N,M,P, mid):
            hi = mid
        else:
            lo = mid

    return mid

if __name__ == "__main__":
    # print "{:0.10f}".format(solve(20000000, 12, 6.8))
    # print pay_all_debt(20000000, 12, 6.8, 2343750.0)
    rl = lambda : sys.stdin.readline().rstrip(' \t\r\n\0')
    for i in xrange(int(rl())):
        N, M, P = rl().split()
        N, M, P = float(N), int(M), float(P)
        print "{:0.10f}".format(solve(N, M, P))
