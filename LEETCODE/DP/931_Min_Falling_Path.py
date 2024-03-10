class Solution(object):
    def minFallingPathSum(self, matrix):
        if len(matrix) < 1: return 0
        
        sol_matrix = matrix
        sol_matrix.append([0] *len(matrix[0]))
        print(sol_matrix)

        for row in range(len(sol_matrix)-2,-1,-1):
            for col in range(0, len(sol_matrix[row])):
                x = sol_matrix[row][col]
                if len(sol_matrix[row]) == 1:
                    sol_matrix[row][col] = x+sol_matrix[row+1][col]
                elif col == 0:
                    sol_matrix[row][col] = min(x+sol_matrix[row + 1][col],
                                            x+sol_matrix[row + 1][col + 1])
                elif col == len(sol_matrix[row])-1:
                    sol_matrix[row][col] = min(x+sol_matrix[row + 1][col - 1],
                                    x+sol_matrix[row + 1][col])
                else:
                    sol_matrix[row][col] = min(x+sol_matrix[row + 1][col - 1],
                                    x+sol_matrix[row + 1][col],
                                    x+sol_matrix[row + 1][col + 1])

        return min(sol_matrix[0])
    
sol = Solution()
matrix = [[-19,57],[-40,-5]]
print(sol.minFallingPathSum(matrix))