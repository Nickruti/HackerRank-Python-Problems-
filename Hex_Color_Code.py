#https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
for _ in range(n):
    hexCode = input()
    if re.search(r'^\s.*(#[\da-fA-F]{3,6})', hexCode):
        print(*re.findall(r'#[\da-fA-F]{3,6}', hexCode), sep='\n')
    
