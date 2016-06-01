import sys
import fnmatch


if __name__ == "__main__":
	rl = lambda: sys.stdin.readline().rstrip('\t\r\n\0')
	for _ in xrange(int(rl())):
		w = rl()
		names = []
		for _ in xrange(int(rl())):
			names.append(rl())

		ret = fnmatch.filter(names, w)
		ret.sort()

		for i in ret:
			print i