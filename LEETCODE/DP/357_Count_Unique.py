class Solution:
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1

        visited = {0: 1}
        for i in range(1,n+1):
            val = 1
            multiples = [9,9,8,7,6,5,4,3,2,1]
            for j in range(0, i):
                val = val*multiples[j]
            visited[i] = visited[i-1] + val
        return visited[n]
    
sol = Solution()
print(sol.countNumbersWithUniqueDigits(2))