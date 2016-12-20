def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    # I = one
    # V = 5
    # X = 10
    # L = 50
    # C = 100
    # D = 500
    # M = 1000
    possible_values = [1000, 500, 100, 50, 10, 5, 1]
    numerals = {
        1 : "I",
        5 : "V",
        10 : "X",
        50 : "L",
        100 : "C",
        500 : "D",
        1000 : "M"
    }
    subtraction = {
        1000: 100,
        500: 100,
        100: 10,
        50: 10,
        10: 1,
        5: 1
    }

    output_string = ""

    while num > 0:
        for val in possible_values:
            if num/val > 0:
                count = num/val
                for _ in xrange(count):
                    output_string += numerals[val]
                num -= count*val
                break
            if num/(val - subtraction[val]) == 1:
                output_string += numerals[subtraction[val]] + numerals[val]
                num -= val - subtraction[val]
                break

    return output_string

print intToRoman(1)
print intToRoman(3999)
print intToRoman(45)