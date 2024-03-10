class Solution:
    def uniquePaths(self, arr):
        m = len(arr)
        n = len(arr[0])

        sol = [[0] * n] * m
        print(sol)

        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                # If finish
                if row == m-1 and col == n-1:
                    sol[row][col] = arr[row][col]
                    continue
                
                current = arr[row][col]
                if row == m-1:
                    sol[row][col] = current + sol[row][col+1]
                elif col == n-1:
                    sol[row][col] = current + sol[row+1][col]
                else: 
                    # Choice between down and right
                    sol[row][col] = current + min(sol[row + 1][col], sol[row][col + 1])
        
        return sol[0][0]

sol = Solution()
arr = [[1,2,3],[4,5,6]]
print(sol.uniquePaths(arr))