import sys

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()

    for _ in xrange(int(rl())):
        rl()
        russia = map( int, rl().split())
        korea = map(int, rl().split())

        russia = sorted(russia,reverse=True)
        korea = sorted(korea,reverse=True)
        i, j, win = 0, 0, 0

        while True:
            if i == len(russia) or  j == len(korea):
                break

            if russia[i] <= korea[j]:
                i+=1
                j+=1
                win += 1
            else:
                i+=1

        print  win
