"""
This script is calculating the modular product of all elements in the array.
Instead of multiplying all the large numbers together
first (which could cause overflow issues with massive numbers),
it uses the modular arithmetic distribution property:
                (A * B) % N = ((A % N) * (B % N)) % N
"""

"""

 > Summary of what this achieves:

This algorithm is used in cryptography and hashing functions. 
It safely computes the remainder of a product of an array of 
numbers relative to n without risking an integer overflow by keeping 
the running product mul bounded under the value of n at all times.
"""

"""
• Iteration 1 (num = 100): mul = (1 * (100 % 11)) % 11  ->  (1 * 1) % 11 = 1
• Iteration 2 (num = 10): mul = (1 * (10 % 11)) % 11    ->  (1 * 10) % 11 = 10
• Iteration 3 (num = 5): mul = (10 * (5 % 11)) % 11     ->  (10 * 5) % 11 = 50 % 11 = 6
• Iteration 4 (num = 25): mul = (6 * (25 % 11)) % 11    ->  (6 * 3) % 11 = 18 % 11 = 7
• Iteration 5 (num = 35): mul = (7 * (35 % 11)) % 11    ->  (7 * 2) % 11 = 14 % 11 = 3
• Iteration 6 (num = 14): mul = (3 * (14 % 11)) % 11    ->  (3 * 3) % 11 = 9 % 11 = 9

"""

#----> 1. Using Modular Multiplication
arr = [100, 10, 5, 25, 35, 14]
n = 11
mul = 1
for num in arr:
    mul = (mul * (num % n)) % n

print(f'Remainder: {mul}')


#-------------------------------------------------------------------------------------------------------------
#----> 2. Using functools.reduce
"""
The functools.reduce() function is used to apply a function of two arguments cumulatively to 
the items of a sequence, reducing the sequence to a single value.
"""
from functools import reduce

arr = [100, 10, 5, 25, 35, 14]
n1 = 11

rem = reduce(lambda x, y: (x * y) % n1, arr)
print(f'Remainder: {rem}')


"""

Step	Operation (x = Accumulator, y = Next Element)	        Process	Result              (x for next step)
----    ---------------------------------------------           --------------              ----------------
1	Takes the first two numbers: 100 and 10	            = (100 * 10) % 11 --->  1000 % 11	    10
2	Combines previous result 10 with next element 5	    = (10 * 5) % 11   ---> 50 % 11      	6
3	Combines previous result 6 with next element 25	    = (6 * 25) % 11   ---> 150 % 11     	7
4	Combines previous result 7 with next element 35	    = (7 * 35) % 11   ---> 245 % 11     	3
5	Combines previous result 3 with final element 14	= (3 * 14) % 11   ---> 42 % 11          9

"""


#-------------------------------------------------------------------------------------------------------------
#----> 3. Naive Multiplication

arr = [100, 10, 5, 25, 35, 14]
n = 11
product = 1

for num in arr:
    product *= num

print(f'Remainder: {product % n}')