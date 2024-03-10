class Solution:
    def uniquePaths(self, m, n):
        sol = [[1] * n] * m
        print(sol)

        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                # If finish
                if row == m-1 and col == n-1:
                    continue
                
                if row == m-1:
                    sol[row][col] = sol[row][col+1]
                elif col == n-1:
                    sol[row][col] = sol[row+1][col]
                else: 
                    # Choice between down and right
                    sol[row][col] = sol[row + 1][col] + sol[row][col + 1]
        
        return sol[0][0]

sol = Solution()
print(sol.uniquePaths(3,7))