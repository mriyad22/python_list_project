"""
1. What is 'Monotonic'?
    An array or list is considered monotonic if it is either entirely non-decreasing or entirely non-increasing.

    * Non-decreasing (equal or increasing): Each element in the array is less than
    or equal to the element that follows it (A[i] <= A[i+1]).

        Example: [1, 2, 2, 3] (Here, the values either increase or stay the same—no element decreases—so it is monotonic.)

    * Non-increasing (staying the same or decreasing): Each element in the array is greater than
    or equal to the element that follows it (A[i] >= A[i+1]).

        Example: [3, 2, 1, 1] (Here, the values are decreasing or staying the same, so it is also monotonic.)


2. Which one is not monotonic?
    If the values in an array increase and then decrease, it is not monotonic.

        Example: [1, 3, 2] (Here, it goes from 1 to 3—an increase—and then from 3 to 2—a decrease.
                Therefore, it is not monotonic.)
"""


#--> 1. Using Single Pass

# arr = [6, 5, 4, 4]
# n = len(arr)
#
# incr = all(arr[i] <= arr[i+1] for i in range(n-1))  #The 'all()' function checks whether all elements in an
# decr = all(arr[i] >= arr[i+1] for i in range(n-1))  #iterable object (such as a list, tuple, set, etc.) are true.
#
# print(incr or decr)


#-------------------------------------------------------------------------

#--> 2. Using Direction Variable

# arr = [6, 5, 4, 4]
# n = len(arr)
#
# if n <= 2:
#     print(True)
# else:
#     d = arr[1] - arr[0]
#     m = True
#     for i in range(2, n):
#         if d == 0:
#             d = arr[i] - arr[i - 1]
#             continue
#         if (d > 0 and arr[i] < arr[i - 1]) or (d < 0 and arr[i] > arr[i - 1]):
#             m = False
#             break
#     print(m)


#-------------------------------------------------------------------------

#--> 3. Using Function

# def is_monotonic(a):
#     return (
#         all(a[i] <= a[i+1] for i in range(len(a) - 1)) or
#         all(a[i] >= a[i+1] for i in range(len(a) - 1))
#     )
#
# print(is_monotonic([1, 2, 2, 3]))
# print(is_monotonic([1, 3, 2]))

#-------------------------------------------------------------------------
#-----> 4. Using zip()
"""
zip(arr, arr[1:]): pairs each element with the next one.
"""

arr = [8, 5, 3, 2, 2]
incr = all(a <= b for a, b in zip(arr, arr[1:]))
decr = all(a >= b for a, b in zip(arr, arr[1:]))
print(incr or decr)


#-------------------------------------------------------------------------
#--> 5. Using Sorting
"""
sorted: creates an ascending version of the array.
"""
arr = [8, 5, 3, 2, 2]
incr = sorted(arr) == arr
decr = sorted(arr, reverse=True) == arr

print(incr or decr)