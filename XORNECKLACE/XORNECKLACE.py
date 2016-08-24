import sys

# XOR has always positive value
# So, Maximum is always using full-length necklace

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()

    for _ in xrange(int(rl())):
        N = int(rl())
        necklace  = map(int, rl().split())
        ret = 0
        for i in xrange(len(necklace)):
            ret += necklace[i-1]^necklace[i]

        print ret

# Below anser is dynamic programing solution
# But, memory limit exceeded because cache
#
# necklace = None
# cache = None
#
# def solve(visited):
#     t = tuple(visited)
#     if t in cache:
#         return cache[t]
#
#
#     bead_list = []
#     for i in xrange(len(visited)):
#         if visited[i]:
#             bead_list.append(i)
#
#     if len(bead_list) == 1:
#         return 0
#
#     ret = 0
#     for i in xrange(len(bead_list)):
#         ret +=  necklace[bead_list[i-1]]^necklace[bead_list[i]]
#
#     for i in xrange(len(visited)):
#         if visited[i]:
#             visited[i] = False
#             ret = max(ret, solve(visited))
#             visited[i] = True
#
#     cache[t] = ret
#     return ret
#
# if __name__ == "__main__":
#     rl = lambda : sys.stdin.readline()
#
#     for _ in xrange(int(rl())):
#         N = int(rl())
#         necklace  = map(int, rl().split())
#         visited = [True] * len(necklace)
#         cache = dict()
#         print solve(visited)
#         print cache
