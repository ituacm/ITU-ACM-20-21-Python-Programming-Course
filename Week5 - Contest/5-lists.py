if __name__ == '__main__'
    arr = []
    N = int(input())
    for i in range(N)
        s = input().split()
        if s[0] == "append"
            arr.append(int(s[1]))
        elif s[0] == "insert"
            arr.insert(int(s[1]),int(s[2]))
        elif s[0] == "remove"
            arr.remove(int(s[1]))
        elif s[0] == "pop"
            arr.pop()
        elif s[0] == "sort"
            arr.sort()
        elif s[0] == "reverse"
            arr.reverse()
        elif s[0] == "print"
            print (arr)
