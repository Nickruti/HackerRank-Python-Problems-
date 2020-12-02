'''
You have an empty sequence, and you will be given  queries. Each query is one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.
Input Format

The first line of input contains an integer, . The next  lines each contain an above mentioned query. (It is guaranteed that each query is valid.)

Constraints



Output Format

For each type  query, print the maximum element in the stack on a new line.

Sample Input

10
1 97
2
1 20
2
1 26
1 20
2
3
1 91
3
Sample Output

26
91
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
stack = []
max_ = 0
for i in range(n):
    query = list(map(int, input().split()))
    if query[0] == 1:
        stack.append(query[1])
        if query[1] > max_:
            max_ = query[1]
            
    elif query[0] == 2:
        top = stack.pop()
        if top == max_:
            if len(stack)==0:
                max_ = 0
                continue
            max_ = max(stack)
        
    elif query[0] == 3:
        print(max_)
