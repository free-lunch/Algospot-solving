import sys

d = {'%24':'$','%25':'%','%20':' ','%21':'!','%28':'(','%29':')','%2a':'*'}
if __name__ == "__main__":
    rl = lambda : sys.stdin.readline().rstrip(' \t\r\n\0')
    for _ in xrange(int(rl())):
        uri = rl()
        ret = ""
        i = 0
        while i < len(uri):
            if uri[i] == "%":
                ret += d[uri[i:i+3]]
                i += 3
            else:
                ret += uri[i]
                i += 1
        print ret
