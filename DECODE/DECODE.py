import sys

def solve(r, c, s):
    pos = 0
    str_list = []
    direction = 0
    dir_list = [1, c,-1, -c]

    for i in xrange(r*c/5):
        one_char = 0
        for j in xrange(4,-1,-1):
            if s[pos] == "1":
                one_char += (1<<j)
            s[pos] = -1
            pos += dir_list[direction]
            need_change_dir = False

            # Case : Visit string at matrix outside
            if direction == 0 and pos == c:
                need_change_dir = True
            elif direction == 1 and pos == len(s)-1+c:
                need_change_dir = True
            # Case : Visit already visted string
            elif s[pos] == -1:
                need_change_dir = True

            if need_change_dir:
                pos -= dir_list[direction]
                direction = (direction+1)%4
                pos += dir_list[direction]

        str_list.append(one_char)

    ret = ""
    for c in str_list:
        if c == 0:
            ret += " "
        else:
            ret += chr(64+c)

    return ret

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline().rstrip(' \t\r\n\0')
    for i in xrange(int(rl())):
        input = rl().split()
        r, c = int(input[0]), int(input[1])
        print i+1, solve(r, c, list(input[2]))
