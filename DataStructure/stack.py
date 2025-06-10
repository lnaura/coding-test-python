import sys
input = sys.stdin.readline

n = int(input())
st = []
for i in range(n):
    command = list(input().split())

    if command[0] == "push":
        st.append(int(command[1]))
    
    if command[0] == "pop":
        
        if st :
            num = st.pop()
            print(num)
        else:
            print(-1)        
    
    if command[0] == "size":
        print(len(st))
    
    if command[0] == "empty":
        if st :
            print(0)
        else:
            print(1) 

    if command[0] == "top":
        if st :
            print(st[len(st)-1])
        else:
            print(-1) 