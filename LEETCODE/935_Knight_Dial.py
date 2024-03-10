# Solution 1 -> TOO LONG!!!
# class Solution(object):
#     def knightDialer(self, n):
#         # visited = {}
#         possibleMoves = [
#             [4,6], #0
#             [6,8], #1
#             [7,9],
#             [4,8],
#             [3,9,0],
#             [],
#             [1,7,0],
#             [2,6],
#             [1,3],
#             [2,4],
#         ]

#         # Base cases
#         if n == 0: 
#             # visited[0] = 0 
#             return 0
#         if n == 1: 
#             # visited[1] = 10 
#             return 10 
#         else:
#             queue = [] 
#             for i in range(0,10): 
#                 queue.append(str(i)) 
            
#             for i in range(2,n+1):
#                 print("")
#                 print(queue)
#                 j=0
#                 while len(queue[0]) < i:
#                     current = queue.pop(0)
#                     last = str(current)[len(current)-1]
#                     print("LAST DIGIT", last)
#                     for k in possibleMoves[int(last)]:
#                         next = current+str(k)
#                         queue.append(next)
            
#             print(queue)
#             return len(queue)
        
# sol = Solution()
# print(sol.knightDialer(4))


class Solution:
    def knightDialer(self, n):     
        arr = [1 for _ in range(10)]
        print(arr)
        
        for i in range(1,n):
            print(i)

            tmp = [
                arr[4]+arr[6],
                arr[6]+arr[8],
                arr[7]+arr[9],
                arr[4]+arr[8],
                arr[3]+arr[9]+arr[0],
                0,
                arr[1]+arr[7]+arr[0],
                arr[2]+arr[6],
                arr[1]+arr[3],
                arr[2]+arr[4]
            ]
            
            arr = tmp
            print(arr)
        
        return sum(arr)%(10**9+7)
        
sol = Solution()
print(sol.knightDialer(4))