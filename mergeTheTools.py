import textwrap
def merge_the_tools(string, k):
    # your code goes here
    if len(string)%k==0:
        myset = set()
        x = textwrap.wrap(string, k)
        for i in range(0, len(x)):
            a = x[i]
            char_seen = []
            for char in a:
                if char not in char_seen:
                    char_seen.append(char)
            print(''.join(char_seen))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)