if __name__ == '__main__':
    N = int(input())
    inputlist = []
    outputlist = []
    for a in range(0, N):
        inputlist.append(input().split())
        if "insert" in inputlist[a][0]:
            i = int(inputlist[a][1])
            e = int(inputlist[a][2])
            outputlist.insert(i,e)
        elif "print" in inputlist[a][0]:
            print(outputlist)
        elif "remove" in inputlist[a][0]:
            x = int(inputlist[a][1])
            outputlist.remove(x)
        elif "append" in inputlist[a][0]:
            x = int(inputlist[a][1])
            outputlist.append(x)
        elif "sort" in inputlist[a][0]:
            outputlist.sort()
        elif "pop" in inputlist[a][0]:
            outputlist.pop()
        elif "reverse" in inputlist[a][0]:
            outputlist.reverse()
