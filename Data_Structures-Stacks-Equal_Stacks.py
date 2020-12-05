'''
You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they're all the same height, then print the height. The removals must be performed in such a way as to maximize the height.

Note: An empty stack is still a stack.

Input Format

The first line contains three space-separated integers, , , and , describing the respective number of cylinders in stacks , , and . The subsequent lines describe the respective heights of each cylinder in a stack from top to bottom:

The second line contains  space-separated integers describing the cylinder heights in stack . The first element is the top of the stack.
The third line contains  space-separated integers describing the cylinder heights in stack . The first element is the top of the stack.
The fourth line contains  space-separated integers describing the cylinder heights in stack . The first element is the top of the stack.
Constraints

Output Format

Print a single integer denoting the maximum height at which all stacks will be of equal height.

Sample Input

5 3 4
3 2 1 1 1
4 3 2
1 1 4 1
Sample Output

5
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    # Write your code here
    max_iteration = len(h1)+len(h2)+len(h3)
    i = 0
    sum_h1 = sum(h1)
    sum_h2 = sum(h2)
    sum_h3 = sum(h3)
    while i < max_iteration:
        
        if sum_h1 > (sum_h2 and sum_h3):
            top = h1.pop(0)
            sum_h1 = sum_h1 - top
            
        elif sum_h2 > (sum_h1 and sum_h3):
            top = h2.pop(0)
            sum_h2 = sum_h2 - top
            
        elif sum_h3 > (sum_h1 and sum_h2):
            top = h3.pop(0)
            sum_h3 = sum_h3 - top
            
        elif sum_h1 == sum_h2 and sum_h1 > sum_h3:
            top1 = h1.pop(0)
            top2 = h2.pop(0)
            sum_h1 = sum_h1 - top1
            sum_h2 = sum_h2 - top2
        
        elif sum_h1 == sum_h3 and sum_h1 > sum_h2:
            top1 = h1.pop(0)
            top3 = h3.pop(0)
            sum_h1 = sum_h1 - top1
            sum_h3 = sum_h3 - top3
        
        elif sum_h2 == sum_h3 and sum_h2 > sum_h1:
            top2 = h2.pop(0)
            top3 = h3.pop(0)
            sum_h2 = sum_h2 - top2
            sum_h3 = sum_h3 - top3
            
        elif sum_h1 == sum_h2 and sum_h1 < sum_h3:
            top = h3.pop(0)
            sum_h3 = sum_h3 - top
        
        elif sum_h1 == sum_h3 and sum_h1 < sum_h2:
            top = h2.pop(0)
            sum_h2 = sum_h2 - top
        
        elif sum_h2 == sum_h3 and sum_h2 < sum_h1:
            top = h1.pop(0)
            sum_h1 = sum_h1 - top
        
        if sum_h1 == sum_h2 == sum_h3:
            return sum_h1
        
        i = i + 1
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
