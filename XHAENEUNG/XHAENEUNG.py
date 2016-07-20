import sys
str_to_int = {"zero":0, "one":1, "two":2, "three":3, "four":4,\
                "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10}
int_to_str = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', \
                5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten'}


if __name__ == "__main__":
    rl = lambda : sys.stdin.readline().rstrip(' \t\r\n\0')
    for i in xrange(int(rl())):
        x, oper, y, _, result = rl().split()

        if oper == "+":
            ret = str_to_int[x] + str_to_int[y]
        elif oper == "-":
            ret = str_to_int[x] - str_to_int[y]
        elif oper == "*":
            ret = str_to_int[x] * str_to_int[y]

        if not (0<=ret<=10):
            print "No"
            continue
            
        if sorted(int_to_str[ret]) == sorted(result):
            print "Yes"
        else:
            print "No"
