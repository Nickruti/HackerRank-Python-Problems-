#https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
for i in range(0, n):
    mobNum = str(input())
    if len(mobNum) != 10:
        print("NO")
    elif len(re.findall("^(7|8|9)", mobNum)) == 0:
        print("NO")
    elif len(re.findall("\d", mobNum)) != 10:
        print("NO")
    else:
        print("YES")
        
    
