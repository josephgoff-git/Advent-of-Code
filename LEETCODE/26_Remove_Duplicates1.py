class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        removed = []
        for i in range(len(nums)):
            if nums[i] not in removed: 
                removed.append(nums[i])
        return removed
    
sol = Solution()
array = [1, 2, 3, 3]
result= sol.removeDuplicates(array)
print(result)