from collections import deque

m, n, h = map(int, input().split())
tomato = []

for i in range(h):
    buf  = []
    for j in range(n):
        buf.append(list(map(int, input().split())))
    tomato.append(buf)
    
dx = [0, 0, 1,-1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = deque()

for i in range(h):
    for j in range(n):
        for l in range(m):
            if tomato[i][j][l] == 1:
                queue.append([i, j, l])

def search():
    ans = 0 
    for i in tomato:
        for j in i:
            for l in j:
                if l == 0:
                    return -1
                ans = max(ans,l)
    return ans-1    

def day():
    while queue:
        a, b, c = queue.popleft()
        for i in range(6):
            z = a+dz[i]
            y = b+dy[i]
            x = c+dx[i]
            if 0 <= z < h and  0 <= y < n and 0 <= x < m:
                if tomato[z][y][x] == 0:
                    tomato[z][y][x] = tomato[a][b][c] + 1
                    queue.append([z,y,x])
    print(search())

day()