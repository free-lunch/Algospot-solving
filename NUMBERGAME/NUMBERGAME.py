import sys

board = None
cache = None
n = 0
MAX = 987654321

def dp(left, right):
    if not cache[left][right] is None:
        return cache[left][right]

    if left == right:
        cache[left][right] = board[left]
        return cache[left][right]
    elif (right - left) == 1:
        if board[left] > board[right]:
            diff = board[left] - board[right]
        else:
            diff = board[right] - board[left]

        cache[left][right] = diff
        return cache[left][right]
    else:
        # 4 cases
        ret = -MAX
        # Delete left 2
        ret = max(ret, -dp(left+2, right))
        # Delete right 2
        ret = max(ret, -dp(left, right-2))
        # Gain left 1
        ret = max(ret, board[left] - dp(left+1, right))
        # Gain right 1
        ret = max(ret, board[right] - dp(left, right-1))

        cache[left][right] = ret
        return cache[left][right]



def solve():
    return dp(0, n-1)

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline().rstrip(' \t\r\n\0')
    for _ in xrange(int(rl())):
        n = int(rl())
        cache = [[None]*n for _ in xrange(n)]
        board = map(int, rl().split())
        print solve()
