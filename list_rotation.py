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



#=====================================================================
"""
plit the Array and Add First Part to the End
"""

#----> 1. Using deque.rotate() from collections
'''
The primary function of a deque (double-ended queue) is to perform a circular 
rotation of the elements in a list—either to the left or to the right.
'''

from  collections import deque

arr = [12, 10, 5, 6, 52, 36]
k = 2

d = deque(arr) #  converts the list into a double-ended queue
d.rotate(-k)    # It will turn 2 spaces to the left.
print(list(d))



#---------------------------------------------------------------------------------

#----> 2. Using List Slicing
arr = [12, 10, 5, 6, 52, 36]
k = 2

arr = arr[k:] + arr[:k]
print(arr)

#---------------------------------------------------------------------------------

#----> 3. Using List Comprehension and Modulo
"""
Formula = (i + k) % n
divide any number by 6, the remainder will always be between 0 and 5.
"""

"""
happens inside the loop:

range(6), the value of `i` in the loop will range from 0 to 5.

1. When i = 0 (1st position in the new list):
    • Formula: (0 + 2) % 6 = 2 % 6 = 2
    • Element: arr[2], which is 5, will be placed here.
2. When `i = 1` (2nd position in the new list):
    • Formula: (1 + 2) % 6 = 3 % 6 = 3
    • Element: arr[3], which is 6, will be placed here.
3. When i = 2 (3rd position in the new list):
    • Formula: (2 + 2) % 6 = 4 % 6 = 4
    • Element: arr[4], which is 52, will be placed here.
4. When i = 3 (4th position in the new list):
    • Formula: (3 + 2) % 6 = 5 % 6 = 5
    • Element: arr[5], which is 36, will be placed here.
    
5. When i = 4 (5th position in the new list — here’s where the magic happens):
    • Formula: (4 + 2) % 6 = 6 % 6 = 0 (dividing 6 by 6 leaves a remainder of 0)
    • Element: arr[0], which is 12, will be placed here. (Notice how the first element has moved to the end!)
6. When i = 5 (last position in the new list):
    • Formula: (5 + 2) % 6 = 7 % 6 = 1 (dividing 7 by 6 leaves a remainder of 1)
    • Element: arr[1], which is 10, will be placed here.
"""
arr = [12, 10, 5, 6,  52, 36]
k = 2

n = len(arr)
result = [arr[(i + k) % 6] for i in range(n)]
print(result)


#---------------------------------------------------------------------------------

#---> 4. Using extend()

arr = [12, 10, 5, 6, 52, 36]
k = 2

a = arr[:k]
b = arr[k:]
b.extend(a)
print(b)