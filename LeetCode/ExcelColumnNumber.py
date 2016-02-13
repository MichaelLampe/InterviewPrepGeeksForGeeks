def titleToNumber(s):
	"""
	:type s: str
	:rtype: int
	"""
	number = 0
	# Reverse string or we could count backwards
	s = s[::-1]
	for index, c in enumerate(s):
		if index == 0:
			number += get_character_number(c)
		else:
			number += (26 ** index)*get_character_number(c)
	return number

def get_character_number(char):
	return ord(char) - 64


print titleToNumber("AAA")
