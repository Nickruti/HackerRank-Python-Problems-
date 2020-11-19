#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    count=0 
    leader = q[0]
    for i in range(0,len(q)): 
        key=q[i]
        if (key > leader):
            leader = key
        if (leader-i-1) > 2:
            return "Too chaotic"
        jj=i
        while(jj>0 and q[jj-1]>key): 
            q[jj]=q[jj-1] 
            jj=jj-1 
            count += 1
                
        q[jj]=key 
    return count  
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        ans = minimumBribes(q)
        print(ans)
