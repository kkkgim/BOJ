

# 7569번 - 토마토 


from collections import deque

# 값 받아오기 
m, n, h = map(int, input().split())
tomato = []

for i in range(h):
    buf  = []
    for j in range(n):
        buf.append(list(map(int, input().split())))
    tomato.append(buf)
    
#앞, 뒤, 오, 왼, 위, 아래
dx = [0, 0, 1,-1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = deque()

#익은 토마토 찾기
for i in range(h):
    for j in range(n):
        for l in range(m):
            if tomato[i][j][l] == 1:
                queue.append([i, j, l])

 #날짜 계산 
def search():
    ans = 0 
    # 안익은 토매이토 검사와 최대값 검사를 같이 ! 효율을 높히자 ! 
    for i in tomato:
        for j in i:
            for l in j:
                # 안익은 토마토가 있다면 바로 리턴
                if l == 0:
                    return -1
                # 안익은 토마토가 없다면 최대값 확인
                ans = max(ans,l)
    return ans-1    


#토마토 익는중
def day():
    while queue:
        a, b, c = queue.popleft()
        for i in range(6):
            # 인덱스 범위 검사
            z = a+dz[i]
            y = b+dy[i]
            x = c+dx[i]
            if 0 <= z < h and  0 <= y < n and 0 <= x < m:
                if tomato[z][y][x] == 0:
                    tomato[z][y][x] = tomato[a][b][c] + 1
                    queue.append([z,y,x])
    print(search())

day()

# 계속 시간초과라고 떠서 솔루션을 찾아보니 " 잔역변수 참조가 지역변수 참조보다 느려서 이게 큰 효과가 있는 코드가 많습니다. " 라는 문구 발견
# 함수로 묶어서 컴파일해보니 해결 ! 함수로 만드는 습관을 가지자 ! 
# 참고 - https://www.acmicpc.net/board/view/64349