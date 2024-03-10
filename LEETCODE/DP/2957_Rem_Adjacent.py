class Solution(object):
    def removeAlmostEqualCharacters(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
    
        # dp[i] represents the minimum number of operations needed to remove almost-equal characters up to index i
        dp = [0] * n
        
        for i in range(1, n):
            # Calculate the cost of making word[i] different from word[i-1]
            cost = 1 if word[i] == word[i-1] else 0
            
            # Update dp[i] based on whether we make word[i] different from word[i-1]
            dp[i] = min(dp[i-1] + cost, dp[i])
            
            # If there's a chance to make word[i] different from word[i-2], update dp[i] accordingly
            if i >= 2:
                cost = 1 if word[i] == word[i-2] else 0
                dp[i] = min(dp[i-2] + cost, dp[i])
        
        return dp[-1]
        
sol = Solution()
print(sol.removeAlmostEqualCharacters("abbaacc"))