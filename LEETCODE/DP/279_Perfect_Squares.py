# import math 

# class Solution(object):
#     def numSquares(self, n):
#         queue = []
#         visited = set()
#         queue.append((0,0))
#         while queue:
#             number, count = queue.pop(0)
#             for i in range(1, int(math.sqrt(n)) + 1):
#                 next_number = number + i*i
#                 if next_number == n:
#                     return count + 1
#                 if next_number not in visited:
#                     visited.add(next_number)
#                     queue.append((next_number, count + 1))

# sol = Solution()
# print(sol.numSquares(10))




import math 

class Solution(object):
    def numSquares(self, n):
        visited = {}
        queue = []
        queue.append((0,1))
        while queue:
            current, count = queue.pop(0)
            for i in range(1,int(math.sqrt(n)) + 1):
                check = current + i**2
                if check == n:
                    return count
                if check not in visited:
                    visited[check] = count
                    queue.append((check, count+1))


sol = Solution()
print(sol.numSquares(10))