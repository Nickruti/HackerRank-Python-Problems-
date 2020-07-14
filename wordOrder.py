n = int(input())

outer_List = []
for i in range(0, n):
    word = input()
    outer_List.append(word)

int_set = set()
print(len(set(outer_List)))
for i in outer_List:
    if i not in int_set:
        print(outer_List.count(i), end=" ")
        int_set.add(i)

'''from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())'''