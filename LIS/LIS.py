import sys

cache = []
seq = None
def solve(sequence):
	global cache
	global seq

	seq = sequence
	n = len(seq)
	cache = [-1] * n
	for i in xrange(n-1,-1,-1):
		lis(i)
	return  max(cache)

def lis(index):
	global seq
	if cache[index] != -1:
		return cache[index]

	cache[index]= 1
	for i in xrange(index+1,len(seq)):
		if seq[index] < seq[i]:
			cache[index] = max(cache[index], lis(i)+1)

	return cache[index]

if __name__ == "__main__":
	rl = lambda: sys.stdin.readline().rstrip('\t\r\n\0')

	for _ in xrange(int(rl())):
		rl()
		print solve(map(int, rl().split()))
