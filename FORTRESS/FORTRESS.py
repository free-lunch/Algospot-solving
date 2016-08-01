import sys
import operator

# Calculate distance between 2 nodes
def dist_node(tree, a, b):
    if a == b:
        return -1

    ret = 0
    # Always depth of a is bigger than depth of b
    if tree[a][1] < tree[b][1]:
        a, b = b, a

    a_depth = tree[a][1]
    b_depth = tree[b][1]
    while a_depth != b_depth:
        a = tree[a][0]
        a_depth = tree[a][1]
        ret += 1

    while a != b:
        a = tree[a][0]
        b = tree[b][0]
        ret += 2

    return ret

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline().rstrip(' \t\r\n\0')

    for _ in xrange(int(rl())):
        n = int(rl())
        walls = [None]*n
        tree = [[0,0] for _ in xrange(n)]
        for i in xrange(n):
            input = map(int, rl().split())
            walls[i] = input[2], input[0], input[1]

        if n < 4:
            print n-1
            continue

        # Make a tree : [parent, depth]
        walls = sorted(walls, reverse=True)
        leaf_nodes = [True]*n
        for i in xrange(n):
            for j in xrange(i+1, n):
                dist = ((walls[i][1]-walls[j][1])**2 + (walls[i][2]-walls[j][2])**2)**0.5
                if walls[i][0] >= dist + walls[j][0]:
                    leaf_nodes[i] = False
                    tree[j][0] = i
                    tree[j][1] += 1

        leaf_nodes = [i for i in xrange(n) if leaf_nodes[i]]
        # print dist_node(tree, leaf_nodes[0],leaf_nodes[1])

        ret = 0
        for i in xrange(len(leaf_nodes)):
            for j in xrange(i+1, len(leaf_nodes)):
                ret = max(ret, dist_node(tree, leaf_nodes[i], leaf_nodes[j]))

        print ret
        #
        #
        # d = dict()
        # for i in xrange(n-1,0,-1):
        #     parent = tree[i][0]
        #     if parent == 0:
        #         if not i in d:
        #             d[i] = 1
        #         continue
        #
        #     while tree[parent][0] != 0:
        #         parent = tree[parent][0]
        #
        #     if parent in d:
        #         d[parent] = max(d[parent], tree[i][1])
        #     else:
        #         d[parent] = tree[i][1]
        #
        # result = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
        # if len(result) == 1:
        #     print result[0][1]
        # else:
        #     print result[0][1] + result[1][1]
