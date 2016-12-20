def trailingZeroes(n):
        """
        :type n: int
        :rtype: int
        """
        final_value = 0
        x = 5
        while x <= n:
            final_value += n/x
            x *= 5

        return final_value

assert trailingZeroes(200) == 49
print "Finished w/o assertion errors"
