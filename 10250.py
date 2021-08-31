T = int(input())
str = []
for i in range(T):
    H,W,N = map(int,input().split())
    if N%H != 0:
        str.append('{0}{1:02d}'.format((N%H), N//H+1))
    else:
        str.append('{0}{1:02d}'.format(H, N//H))
for roomNum in str:
    print(roomNum)