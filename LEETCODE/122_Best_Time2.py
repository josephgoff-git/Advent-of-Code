class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """        
        maxProfit = 0
        lookingForMin = True
        priceBuy = 0 

        for i in range(len(prices)):
            if i == len(prices) - 1:
                if lookingForMin == False:
                    maxProfit += prices[i] - priceBuy
            else: 
                if lookingForMin == True:
                    if prices[i+1] <= prices[i]:
                        continue
                    else:
                        lookingForMin = False
                        priceBuy = prices[i]
                else:
                    if prices[i+1] >= prices[i]:
                        continue
                    else:
                        lookingForMin = True
                        maxProfit += prices[i] - priceBuy

        return maxProfit

sol = Solution().maxProfit([21,3,3,25])
print(sol)