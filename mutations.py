def mutate_string(string, position, character):
    a = list(string)
    a[position] = character
    new = ''.join(a)
    return new

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)