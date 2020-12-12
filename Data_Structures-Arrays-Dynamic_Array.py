'''
Problem url = https://www.hackerrank.com/challenges/dynamic-array/problem

Create a list, seqList, of  empty sequences, where each sequence is indexed from 0 to n-1 . The elements within each of the  sequences also use 0-indexing.
Create an integer,lastAnswer , and initialize it to 0.
There are 2 types of queries that can be performed on the list of sequences:
Query: 1 x y
Find the sequence, seq, at index ((x^lastAnswer)%n) in seqList.
Append integer y to sequence .
Query: 2 x y
Find the sequence, seq, at index ((x^lastAnswer)%n) in seqList.
Find the value of element  in  (where  is the size of ) and assign it to .
Print the new value of  on a new line
Note:  is the bitwise XOR operation, which corresponds to the ^ operator in most languages. Learn more about it on Wikipedia.  is the modulo operator.

Function Description

Complete the dynamicArray function below.

dynamicArray has the following parameters:
- int n: the number of empty sequences to initialize in 
- string queries[q]: an array of query strings

Returns

int[]: the results of each type 2 query in the order they are presented
Input Format

The first line contains two space-separated integers,  (the number of sequences) and  (the number of queries), respectively.
Each of the  subsequent lines contains a query in the format defined above, .

Constraints

It is guaranteed that query type  will never query an empty sequence or index.
Sample Input

2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1
Sample Output

7
3
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    lastAnsList = []
    seq = [[] for i in range(n)]
    lastAnswer = 0
    for i in range(len(queries)):
        index = (queries[i][1] ^ lastAnswer) % n
        if queries[i][0] == 1:
            seq[index].append(queries[i][2])
        else:
            lastAnswer = queries[i][2] % len(seq[index])
            lastAnswer = (seq[index][lastAnswer])
            lastAnsList.append(lastAnswer)
    return lastAnsList
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
