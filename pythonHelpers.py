# default dict --> Give every value a default value using lambda 
from collections import defaultdict
nums = [1,2,3]
counts = defaultdict(lambda: 0)
for num in nums:
    counts[num] += 1

# .get -> get value and add 1, or get 0 (if None) and add 1
    counts[num] = counts.get(num, 0) + 1

# Syntax for conditionals 
    counts[num] = counts[num] + 1 if num in counts else 1 


# Counters
from collections import Counter
c = Counter(nums)
print(max(c, key=lambda k: c[k])) # print the object key with the highest value  (using key=lambda for max/min)

# 
a = [1, 2, 3]
b = [10, 8, 6]
indices = range(len(a)) # create array of indeces 
print(max(indices, key=lambda i: a[i] + b[i])) # print the index such that a + b at that index has highest value 