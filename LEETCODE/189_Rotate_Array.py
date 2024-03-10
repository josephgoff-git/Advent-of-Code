class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(0,k):
            keeplast = nums[-1]
            nums[1:] = nums[:-1]
            nums[0] = keeplast

sol = Solution().rotate([1,2,3,3,3], 3)