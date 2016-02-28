def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0
        for i in xrange(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                profit += prices[i] - prices[i-1]
                i += 1

        return profit

assert maxProfit([2, 1, 3, 1 , 4]) == 5
print "Finished without assertion error"