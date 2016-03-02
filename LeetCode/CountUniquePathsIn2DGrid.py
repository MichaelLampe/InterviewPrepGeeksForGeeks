def uniquePaths(m, n):
	"""
	:type m: int
	:type n: int
	:rtype: int
	"""
	solution_array = [[1] * n for _ in xrange(m)]
	for x in xrange(1, m):
		for y in xrange(1, n):
			solution_array[x][y] = solution_array[x - 1][y] + solution_array[x][y - 1]

	return solution_array[m - 1][n - 1]