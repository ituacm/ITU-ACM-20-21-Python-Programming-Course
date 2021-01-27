t = int(input())
for k in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    a, c, mx, x = [0]*n, [0]*n, 0, 0
    
    for i in range(1, n):
        a[i] = b[i] - b[i-1]
        
    for i in range(1, n):
        c[i] = a[i] - a[i-1]
    
    for i in range(1, n):
        if c[i] == 0:
            x+=1
        else:
            mx = max(mx, x)
            x = 1
    print("Case #"+str(k+1)+ ": "+str(max(mx, x)+1))