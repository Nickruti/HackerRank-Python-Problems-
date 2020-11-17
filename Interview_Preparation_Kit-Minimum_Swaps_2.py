'''
def minimumSwaps(q):
    #counts number of swaps
    count = 0
    for i in range(0,len(q)-1):
        if q[i] == i+1:
            continue
        else:
            element_index = q.index(i+1, i+1)
            #swap
            temp = q[i]
            q[i] = q[element_index]
            q[element_index] = temp
            count += 1
    return count
'''
#This solution has high time complexitysince test case no. 9, 10, 11, 12, 14 did not run.
#Error: Time Out
#number of elements in array were around 50000 or even more

#Improved Solution

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    #counts number of swaps
    count = 0
    for i in range(0,len(arr)-1):
        while arr[i] != i + 1:
            t = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = t
            count += 1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
