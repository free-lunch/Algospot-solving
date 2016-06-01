import sys

class TrianglePath():
	@staticmethod
	def solve(triangle):
		n = len(triangle)
		for i in xrange(n-1,-1,-1):
			for j in xrange(n-1,-1,-1):
				if i < j:
					triangle[j-1][i] += max(triangle[j][i], triangle[j][i+1])

		return triangle[0][0]

if __name__ == "__main__":
	rl = lambda: sys.stdin.readline().rstrip('\t\r\n\0')

	for _ in xrange(int(rl())):
		triangle = []
		for _ in xrange(int(rl())):
			triangle.append(map(int, rl().split()))

		print TrianglePath.solve(triangle)