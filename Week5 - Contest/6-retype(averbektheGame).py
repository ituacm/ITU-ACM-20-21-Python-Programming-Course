t = int(input())
for i in range(1, t+1):
    n, k, s = [int(i) for i in input().split()]
    print("Durum #" + str(i) +": " + str(min(k-s+n-s+k, n+k)))