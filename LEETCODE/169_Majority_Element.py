from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        for item in c:
            if c[item] > len(nums) / 2:
                return item

sol = Solution().majorityElement([1,2,3,3,3])
print(sol)