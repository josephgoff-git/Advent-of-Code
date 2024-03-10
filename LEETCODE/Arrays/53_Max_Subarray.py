class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        maxSum = nums[0]
        currentSum = nums[0]
        
        for i in range(1,len(nums)):
            currentSum += nums[i]
            if nums[i] >= currentSum:
                currentSum = nums[i]

            if currentSum > maxSum:
                maxSum = currentSum
        return maxSum
    
sol = Solution()
arr = [-2,1,-3,4,-1,2,1,-5,4]
arr = [5,4,-1,7,8]
print(sol.maxSubArray(arr))