import sys

def determine(n, c, c_numbers, value):
    cu_sum = 0
    for i in xrange(c):
        cu_sum += min(c_numbers[i], value)
    if cu_sum >= value*n:
        return True
    else:
        return False

def solve(n, c, c_numbers):
    max_bound = sum(c_numbers)+1
    min_bound = 0

    while min_bound + 1 < max_bound:
        mid = (max_bound+min_bound)/2
        if determine(n, c, c_numbers, mid):
            min_bound = mid
        else:
            max_bound = mid

    return min_bound


if __name__ == "__main__":
    rl = lambda : sys.stdin.readline().rstrip(' \t\r\n\0')
    for _ in xrange(int(rl())):
        n, c = map(int, rl().split())
        c_numbers = map(int, rl().split())
        print solve(n, c, c_numbers)
