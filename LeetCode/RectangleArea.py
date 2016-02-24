def computeArea(A, B, C, D, E, F, G, H):
	"""
	:type A: int
	:type B: int
	:type C: int
	:type D: int
	:type E: int
	:type F: int
	:type G: int
	:type H: int
	:rtype: int
	"""

	"""
	Areas of the two individual triangles
	"""
	rect1 = (C - A) * (D - B)
	rect2 = (G - E) * (H - F)
	area = rect1 + rect2
	if C < E or A > G:
		return area

	if B > H or D < F:
		return area

	"""
	Remove overlapping area
	"""
	top = min(C,G)
	bottom = max(A, E)
	right = min(H, D)
	left = max(B, F)

	remove = (top - bottom) * (right - left)
	return rect1 + rect2 - remove
