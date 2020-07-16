import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width) 
    word_list = wrapper.wrap(text=string) 
    for i in word_list[0:-1]:
        print(i)
    return word_list[-1]

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)