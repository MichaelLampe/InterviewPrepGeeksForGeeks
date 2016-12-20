def isAnagram(s, t):
	if s == t:
		return True
	"""
	:type s: str
	:type t: str
	:rtype: bool
	"""
	letters_with_counts = dict()
	for letter in s:
		if letters_with_counts.get(letter) is not None:
			letters_with_counts[letter] += 1
		else:
			letters_with_counts[letter] = 1

	for letter in t:
		# New letter exists
		if letters_with_counts.get(letter) is None:
			return False
		else:
			letters_with_counts[letter] -= 1

	# Final check
	for k in letters_with_counts.keys():
		if letters_with_counts[k] != 0:
			return False

	return True

if __name__ == "__main__":
	assert isAnagram("cat", "rat") == False
	assert isAnagram("okokok", "kokoko") == True
	print "Finished without errors"
