if __name__ == '__main__':
    s = input()

visited = [0,0,0,0,0]
for i in range(0, len(s)):
    if s[i].isalnum():
        visited[0] = 1
    if s[i].isalpha():
        visited[1] = 1
    if s[i].isdigit():
        visited[2] = 1
    if s[i].islower():
        visited[3] = 1
    if s[i].isupper():
        visited[4] = 1
        
for i in visited:
    if i == 1:
        print("True")
    else:
        print("False")
   
    