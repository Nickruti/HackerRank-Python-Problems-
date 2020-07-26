# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = map(int, input().split())

A = defaultdict(list)
for i in range(1, n+1):
    A[input()].append(i)

B = []
for i in range(1, m+1):
    B.append(input())

for i in B:
    if i in A:
        print(*A[i])
    else:
        print("-1")
