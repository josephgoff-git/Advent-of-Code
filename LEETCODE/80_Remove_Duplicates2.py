from collections import Counter, defaultdict

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # deduped = Counter(nums).keys()
        deduped = []
        counts = defaultdict(lambda: 0)
        for i, num in enumerate(nums):
            counts[num] += 1
            if counts[num] <= 2:
                deduped.append(num)
        
        nums.clear()
        nums.extend(deduped)
        return len(deduped)
 
        
sol = Solution()
array = [1,2,3,3,4,4,4,5,5,5,5,1,2]
results = sol.removeDuplicates(array)
print(results)

c = Counter()