"""
Given an array of integers and a number d, the task is to rotate the array to the left by 'd' positions.
In left rotation, each element moves one position to the left, and the first element moves to the end of the array.
"""

#Using List Slicing

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# d = 2
# arr[:] = arr[d:] + arr[:d]
# print(arr)

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
