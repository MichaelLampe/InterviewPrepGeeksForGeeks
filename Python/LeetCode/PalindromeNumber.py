def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        # Can't be negative
        if x < 0:
            return False

        original = x
        reverse = 0

        while original > 0:
            digit = original % 10
            reverse = reverse*10 + digit
            original = original/10
        return x == reverse

assert isPalindrome(121) == True
assert isPalindrome(141) == True
assert isPalindrome(251) == False
assert isPalindrome(25) == False
assert isPalindrome(55) == True
assert isPalindrome(0) == True
assert isPalindrome(-10) == False
print "Finished without assertion error"