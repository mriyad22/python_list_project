"""
Find Largest Element in an Array
"""
#Using Built-in max() Function

arr = [10, 315, 66, 98, 2900, 57]
result = max(arr)
print(result)

#-------------------------------------------------------------------------

#Using Iteration
arr = [10, 315, 66, 98, 2900, 57]
result = arr[0]

for i in range(1, len(arr)):
    if arr[i] > result:
        result = arr[i]

print(result)

#-------------------------------------------------------------------------

#Using reduce() Function

from functools import reduce

arr = [10, 315, 66, 98, 2900, 57]
result = reduce(max, arr)
print(result)

#-------------------------------------------------------------------------

#Using sort() Function

arr = [10, 315, 66, 43, 3020, 90, 18]

arr.sort()
res = arr[-1]
print(res)

#-------------------------------------------------------------------------

#Using operator.gt()
from operator import gt

arr = [10, 315, 66, 43, 3020, 90, 18]
res = 0
for i in arr:
    if gt(i, res):
        res = i

print(res)
