

# 손익분기점 찾기

def profit():
    a,b,c, = map(int,input("").split())
    # 제로 디비전 체크 및 손익분기점이 생기는 조건
    if c-b > 0 :
        result = a//(c-b)+1
        if result > 0 :
            print(a//(c-b)+1)
    else:
        print(-1)

profit()
