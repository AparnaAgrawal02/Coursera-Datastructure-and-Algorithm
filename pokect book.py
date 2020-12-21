import sys
import math
import bisect
input = sys.stdin.readline
############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))
def printlist(var) : sys.stdout.write(' '.join(map(str, var))+'\n')

n,k=invr()
x=[]
d=[[] for i in range(k)]
dd=[0 for i in range(k)]
for i in range(n):
    x.append(input())
for i in range(n):
    for j in range(k):
        if x[i][j] not in d[j]:
            d[j].append(x[i][j])
            dd[j]+=1
ans=1
for i in dd:
    ans*=i
print(ans%1000000007)




