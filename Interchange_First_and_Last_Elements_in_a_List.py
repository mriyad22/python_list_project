"""
The task is to swap the first and last elements of the list without changing the order of the remaining elements.
"""

#----> 1. Using Direct Assignment
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(lst)
# lst[0], lst[-1] = lst[-1], lst[0]
# print(lst)


#-------------------------------------------------------------------
#----> 2. Using Tuple Variable
"""
This method temporarily groups the last and first elements into a tuple before swapping.
"""
# lst = [12, 35, 9, 56, 24]
# pair = lst[-1], lst[0]
# lst[0], lst[-1] = pair
# print(lst)


#-------------------------------------------------------------------
#----> 3. Using the * Operator
"""
This method splits the list into the first element, the middle part, and the last element, 
then places them back in swapped order.
"""

# lst = [3, 8, 23, 2, 11, 90]
# a, *mid, b = lst
# lst = [b, *mid, a]
# print(lst)

#-------------------------------------------------------------------
#-----> 4. Using Slicing
"""
This method creates a new list by rearranging slices so the last element moves to the front and 
the first moves to the end.
"""

lst = [3, 8, 23, 2, 11, 90]
lst = lst[-1:] + lst[1:-1] + lst[:1]
print(lst)

#-------------------------------------------------------------------



#-------------------------------------------------------------------
