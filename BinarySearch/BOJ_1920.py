import sys
input = sys.stdin.readline

n = input().rstrip()
array = list(map(int,input().split()))

m = input().rstrip()
x = list(map(int,input().split()))

def bs(array,target,start,end):
    

    while start > end:
        mid = (start+end) // 2
