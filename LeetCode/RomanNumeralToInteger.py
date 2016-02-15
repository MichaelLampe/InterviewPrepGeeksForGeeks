def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        numeral_value_table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        numeral_list = list(s)
        for i in xrange(len(numeral_list) - 1):
            current_numeral = numeral_list[i]
            next_numeral = numeral_list[i+1]
            if numeral_value_table[current_numeral] < numeral_value_table[next_numeral]:
                total -= numeral_value_table[current_numeral]
            else:
                total += numeral_value_table[current_numeral]
        total += numeral_value_table[numeral_list[-1]]
        return total


assert romanToInt("IV")  == 4
print "Finished without assertion errors"
