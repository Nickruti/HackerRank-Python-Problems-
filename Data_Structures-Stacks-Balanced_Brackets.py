'''
Sample Input

3
{[()]}
{[(])}
{{[[(())]]}}
Sample Output

YES
NO
YES
Explanation

The string {[()]} meets both criteria for being a balanced string, so we print YES on a new line.
The string {[(])} is not balanced because the brackets enclosed by the matched pair { and } are not balanced: [(]).
The string {{[[(())]]}} meets both criteria for being a balanced string, so we print YES on a new line.

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    lenS = len(s)
    if lenS % 2!= 0:
        return 'NO'
    for i in range(lenS):
        if s[i]=='(' or s[i]=='[' or s[i]=='{':
            if i!=lenS-1:
                stack.append(s[i])
            else:
                return 'NO'
        else:
            if len(stack) == 0:
                return 'NO' 
            top = stack.pop()
            if top == '(' and s[i] == ')':
                if len(stack) == 0 and i==lenS-1:
                    return 'YES'
                continue
            elif top == '[' and s[i] == ']':
                if len(stack) == 0 and i==lenS-1:
                    return 'YES'
                continue
            elif top == '{' and s[i] == '}':
                if len(stack) == 0 and i==lenS-1:
                    return 'YES'
                continue
            else:
                return 'NO'
                        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
