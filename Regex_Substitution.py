# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
for _ in range(n):
    s = input()
    print(re.sub(r"(?<=\s)\|{2}(?=\s)",'or',re.sub(r"(?<=\s)&&(?=\s)",'and',s)))
    # Below solution fails for 3 test cases
    # s = re.sub(r'(\s&&\s)'," and ", s)
    # s = re.sub(r'(\s\|\|\s)'," or ", s)
    # print (s)
