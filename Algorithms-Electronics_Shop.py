#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    lenk = len(keyboards)
    lend = len(drives)
    if lenk + lend == 2:
        if keyboards[0] + drives[0] <= b:
            return keyboards[0] + drives[0]
        else:
            return -1
    max_ = 0
    keyboards.sort(reverse=True)
    drives.sort(reverse=True)

    for i in keyboards:
        if i >= b:
            if i == keyboards[lenk-1]:
                return -1
            continue
        for j in drives:
            if j >= b:
                continue
            sum_ = i + j
            if sum_ <= b:
                if sum_ > max_:
                    max_ = sum_
    if max_ == 0:
        return -1
    return max_
                
                
                
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
