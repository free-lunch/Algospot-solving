import sys

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()
    for _ in xrange(int(rl())):
        str1, str2 = rl().split()
        if str1 == str2 or len(str1) != len(str2):
            print("No.")
            continue

        if sorted(str1) == sorted(str2):
            print("Yes")
        else:
            print("No.")
