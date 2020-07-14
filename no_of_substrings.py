def count_substring_my(string, sub_string):
    cnt = 0
    j = 0
    for i in range(0, len(string)):
        if string[i]==sub_string[j]:
            j = j + 1
            if j == len(sub_string):
                if string[i]==sub_string[0]:
                    j = 1
                else:
                    j = 0
                cnt = cnt + 1
    return cnt

def count_substring_geeks(string, sub_string):
    count = 0
    start = 0
    while start < len(string): 
        pos = string.find(sub_string, start) 
        if pos != -1: 
            start = pos + 1
            count += 1
        else:
            break
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring_geeks(string, sub_string)
    print(count)


