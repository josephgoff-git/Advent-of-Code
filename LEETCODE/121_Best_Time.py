class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # maxProfit = 0 
        # for i, price in enumerate(prices):
        #     if i == len(prices) - 1:
        #         return maxProfit
            
        #     for j in range(i+1, len(prices)): 
        #         if prices[j] - price > maxProfit:
        #             maxProfit = prices[j] - price
        highestVal = 0
        maxProfit = 0
        for i in range(len(prices)-1, -1, -1):
            if prices[i] > highestVal:
                highestVal = prices[i]
        
            if i < len(prices) - 1:
                if highestVal - prices[i] > maxProfit:
                    maxProfit = highestVal - prices[i]
        
            if i == 0:
                return maxProfit


sol = Solution().maxProfit([21,3,3,25])
print(sol)