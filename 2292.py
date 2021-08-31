# 벌집

def roomCount():
    # 첫번째방 카운트
    x = int(input())-1
    count = 1
    # 반복 카운트
    while x > 0:
        x = x - (6 * count)
        count = count + 1
    print(count)

roomCount()

