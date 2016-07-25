import sys


def solve(r, c, s):
    bin_list = ""
    for char in s:
        if char == " ":
            bin_list += "00000"
        else:
            bin_list += "{:05b}".format(ord(char)-64)

    pos = 0
    direction = 0
    dir_list = [1, c,-1, -c]
    ret = [-1]*(r*c)
    try:
        for i in xrange(len(bin_list)):
            ret[pos] = bin_list[i]
            pos += dir_list[direction]
            need_change_dir = False

            # Case : Visit string at matrix outside
            if direction == 0 and pos == c:
                need_change_dir = True
            elif direction == 1 and pos >= r*c:
                need_change_dir = True
            # Case : Visit already visted string
            elif ret[pos] != -1:
                need_change_dir = True

            if need_change_dir:
                pos -= dir_list[direction]
                direction = (direction+1)%4
                pos += dir_list[direction]
    except:
        return "0"

    for i in xrange(len(ret)):
        if ret[i] == -1:
            ret[i] = "0"

    return "".join(ret)

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline().rstrip('\t\r\n\0')
    for i in xrange(int(rl())):
        input = rl()
        # for i in xrange(len(input)):
        try:
            r, c, s = input.split(' ', 2)
        except:
            r, c = input.split(' ', 2)
            s = ""

        r, c = int(r), int(c)
        print i+1, solve(r, c, s)
