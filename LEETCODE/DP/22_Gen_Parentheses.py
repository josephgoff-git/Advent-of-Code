class Node(object):
    def __init__(self, val="",left=None, right=None, countL=0, countR=0):
        self.val = val
        self.left = left
        self.right = right
        self.countL = countL
        self.countR = countR

class Solution(object):
    def generateParenthesis(self, n):
        if n == 0: return []
        
        root = Node("(", None, None, 1, 0)
        queue = [root]
        results = []
        while queue: 
            current = queue.pop(0)

            if current.countL < n: 
                current.left = Node(current.val + "(", None, None, current.countL+1, current.countR)
                queue.append(current.left)
            if current.countR < current.countL:
                current.right = Node(current.val + ")", None, None, current.countL, current.countR+1)
                queue.append(current.right)
            
            if current.countL >= n and current.countR >= current.countL: 
                results.append(current.val)
        return results

sol = Solution()
print(sol.generateParenthesis(3))
