def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    if s == "":
        return 0

    s = s.strip()
    split = s.split(" ")
    return len(split[-1])

assert lengthOfLastWord("a ") == 1
assert lengthOfLastWord("") == 0
assert lengthOfLastWord("a") == 1
assert lengthOfLastWord("Hello world") == 5
print "Finished without assertion errors."
