n = int(input())

l = {'A':0, 'B': 1, 'C': 2,'D':3, 'E':4,'F':5,'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11,
     'M':12, 'N':13, 'O':14, 'P':15,'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 
     'X':23, 'Y':24, 'Z':25}

names_set = set()
a = []

for i in range(n):
    b, tot = [0]*26, 0
    x = input() 
    y = x.upper()
    name_list = list(y) 
    for j in range(len(y)):
        if name_list[j] != " ":
            if b[l[name_list[j]]] == 0:
                b[l[name_list[j]]] += 1
                tot+=1       
    a.append([tot, x])
      
sorted_list = sorted(a)

print(str(sorted_list[-1][1]))
