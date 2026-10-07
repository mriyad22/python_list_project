"""
Given an array of integers and a number d, the task is to rotate the array to the left by 'd' positions.
In left rotation, each element moves one position to the left, and the first element moves to the end of the array.
"""

#Using List Slicing

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
d = 2
arr[:] = arr[d:] + arr[:d]
print(arr)

#-------------------------------------------------------------------------
#Using reverse() Method
"""
[::-1] it means reverse
[start : stop : step]

start → Not specified, so it will start from the end
stop → Not specified, so it will go until the beginning
step = -1 → It will move backwards one step at a time

[1, 2, 3, 4, 5] → [::-1] → [5, 4, 3, 2, 1]


"""

arr = [1, 2, 3, 4, 5, 6]
d = 2
n = len(arr)
arr.reverse()

arr[:n-d] = arr[:n-d][::-1]
arr[n-d:] = arr[n-d:][::-1]
print(arr)

#-------------------------------------------------------------------------
#Using Temporary Array

arr = [1, 2, 3, 4, 5, 6]
d = 2
n = len(arr)

temp = arr[:d]
arr[:n-d] = arr[d:]
arr[n-d:] = temp
print(arr)

#-------------------------------------------------------------------------
#One by One Rotation

arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
n = len(arr)

for i in range(d):
    arr.append(arr.pop(0))

print(arr)


#-------------------------------------------------------------------------

"""
Reversal Algorithm for Array Rotation:

Array rotation means shifting array elements to the left or right by a given number of positions.

Example:
        Input:  arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2
        Output:   arr[] = [3, 4, 5, 6, 7, 1, 2] 
"""

"""
Step 1: declare a array
Step 2: define a variable d
Step 3: calculate the length of the array and store it into n 
Step 4: reverses the first 2 elements -> [2, 1, 3, 4, 5, 6, 7]
Step 5: reverses remaining elements -> [2, 1, 7, 6, 5, 4, 3]
Step 6: reverses entire array -> [3, 4, 5, 6, 7, 1, 2]
"""

# 1. Using reverse() Function

arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
n = len(arr)

#Reverse first d elements
arr[d:] = reversed(arr[d:])

#Reverse remaining elements
arr[:d] = reversed(arr[:d])

#Reverse entire array
arr.reverse()
print(arr)



#-------------------------------------------------------------------------

# 2. Using collections.deque

"""
deque from the collections module allows fast appends and pops from both ends. 
It includes a rotate() method that can efficiently rotate elements left or right.
"""

"""
1. Convert list to deque for efficient rotation.
2. Rotate left by d using rotate(-d).
3. Convert back to list and print the result.

"""

from collections import deque

arr = [1, 2, 3, 4, 5, 6, 7]
d = 2

result = deque(arr)
result.rotate(-d)
print(list(result))

#-------------------------------------------------------------------------

# Using Manual Swap Method

arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
n = len(arr)

#reverse first part
start = 0
end = d - 1
while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

#reverse second part
start = d
end = n - 1
while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

#reverse full array
arr.reverse()
print(arr)