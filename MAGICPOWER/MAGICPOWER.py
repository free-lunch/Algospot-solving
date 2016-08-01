import sys
from collections import Counter

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline().rstrip(' \t\r\n\0')
    for _ in xrange(int(rl())):
        N, M = map(int, rl().split())

        items = Counter(map(int, rl().split()))
        index = list(sorted(items))
        ret = 0

        while M > 0:
            # Case : Remain only same value items (Rectangle graph)
            if len(index) == 1:
                if M > items[index[0]]*index[0]:
                    ret +=  sum(range(index[0]+1))*items[index[0]]
                else:
                    x,y = divmod(M, items[index[0]])
                    ret += sum(range(index[0]-x+1, index[0]+1))*items[index[0]]
                    ret += (index[0]-x) * y
                break
                
            # Case : Stepped graph
            # e.g) below shape
            #        -
            #    ----
            # ---
            else:
                n = len(index)-1
                # Calculate a highest value rectangle and then continue this work
                if M > items[index[n]]*(index[n]-index[n-1]):
                    ret += sum(range(index[n-1]+1, index[n]+1))*(items[index[n]])
                    M -= items[index[n]]*(index[n]-index[n-1])
                    items[index[n-1]] += items[index[n]]
                    del items[index[n]]
                    del index[n]
                # Calculate remain M and then finish
                else:
                    x,y = divmod(M, items[index[n]])
                    ret += sum(range(index[n]-x+1, index[n]+1))*items[index[n]]
                    ret += (index[n]-x) * y
                    break

        print ret
