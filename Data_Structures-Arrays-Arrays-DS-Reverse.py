'''
Reverse the array
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    for i in range(int(len(a)/2)):
        temp = a[i]
        a[i] = a[len(a)-i-1]
        a[len(a)-i-1] = temp
        print(i)
    return a
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
'''
Input - 
4
1 4 3 2
Output -
2 3 4 1
'''
