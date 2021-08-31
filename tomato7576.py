count = 1
m, n = map(int,input("입력해주세요!").split((" ")))
tomato = [[0 for col in range(m)] for row in range(n)]
for i in range(n):
    tomato[i] = [int(j) for j in input().split()]
while True:
    check = 0 
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 0 : 
                check = 1 
                break
    if check == 0:
        break
    elif count - max(map(max, tomato)) >= 2 :
        count = 0
        break
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == count:
                if j-1 != -1 : #왼쪽
                    if tomato[i][j-1] == 0:
                        tomato[i][j-1] = count +1 
                if j+1 < m  : #오른쪽
                    if tomato[i][j+1] == 0:
                        tomato[i][j+1] = count +1 
                if i-1 != -1  : #위쪽
                    if tomato[i-1][j] == 0:
                        tomato[i-1][j] = count +1       
                if i+1 < n  : #아래쪽
                    if tomato[i+1][j] == 0:
                        tomato[i+1][j] = count +1 
    count = count + 1     
print( count-1 )