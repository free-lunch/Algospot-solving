import sys

class JumpGame():
	def __init__(self, matrix):
		self.n = len(matrix[0])
		self.cache = [[-1 for _ in xrange(self.n)] for _ in xrange(self.n)]
		self.matrix = matrix

	def solve(self):
		ret = self.jump(0,0)
		if ret is 1:
			return 'YES'
		else:
			return 'NO'

	def jump(self, y, x):
		n = self.n
		if y is n-1 and x is n-1:
			return 1
		if y >= n or x >= n:
			return 0
		if self.cache[y][x] != -1:
			return self.cache[y][x]

		jumpSize = self.matrix[y][x]
		l = self.jump(y+jumpSize, x)
		r = self.jump(y,x+jumpSize)

		if l is 0 and r is 0:
			self.cache[y][x] = 0
		else:
			self.cache[y][x] = 1

		return self.cache[y][x]


if __name__ == "__main__":
	sys.setrecursionlimit(10000)
	rl = lambda: sys.stdin.readline()
	for _ in xrange(int(rl())):
		matrix = []
		for _ in xrange(int(rl())):
			matrix.append(map(int,rl().rstrip(' \t\r\n\0').split(' ')))
		test = JumpGame(matrix)
		print test.solve()


