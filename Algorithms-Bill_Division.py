#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    anna_bill = 0
    false_bill = 0
    for i in range(len(bill)):
        if i != k:
            anna_bill += bill[i]
        false_bill += bill[i]
    anna_bill = anna_bill / 2
    false_bill = false_bill / 2
    if anna_bill == b:
        print ("Bon Appetit")
    else:
        print (int(false_bill - anna_bill))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
