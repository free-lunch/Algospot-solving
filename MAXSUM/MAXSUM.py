import sys

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()
    for _ in xrange(int(rl())):
        n = int(rl())
        array = map(int, rl().split())
        cu_sum, max_value = 0, 0
        for i in xrange(n):
            cu_sum += array[i]
            if cu_sum < 0 and array[i] > 0:
                cu_sum = array[i]
            elif cu_sum < 0 and array[i] < 0:
                cu_sum = 0
            else:
                max_value = max(max_value, cu_sum)
        print max_value
