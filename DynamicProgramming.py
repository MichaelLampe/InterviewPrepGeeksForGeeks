
def longest_common_substring(X, Y):
# Longest Common Subsequence
	memorize = {}
	def lcs(s_1, s_2, index_of_s1, index_of_s2):
		if index_of_s1 == 0 or index_of_s2 == 0:
			return 0

		if memorize.get((index_of_s1, index_of_s2)) is not None:
			return memorize[(index_of_s1, index_of_s2)]
		elif s_1[index_of_s1-1] == s_2[index_of_s2-1]:
			answer = 1 + lcs(s_1, s_2, index_of_s1-1, index_of_s2 - 1)
		else:
			answer = max(
					lcs(s_1, s_2, index_of_s1 - 1, index_of_s2),
					lcs(s_1, s_2, index_of_s1, index_of_s2 - 1)
					)

		memorize[(index_of_s1, index_of_s2)] = answer
		return answer
	return lcs(X, Y, len(X), len(Y))