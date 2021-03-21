# 한번 밟을 때마다 1씩 줄어든다
# 0이 되면 더이상 못밟아 이때는 그 다음 디딤돌로 한번에 여러칸 건너 뛰어
# 밟을 수 있는게 여러개 이면 가장 가까운거

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

count = 0
stack = []
while 1:
    count += 1
    stack = []
    for i in range(len(stones)): #0보다 클때만
        if stones[i] > 0:
            stones[i] -= 1

        if stones[i] == 0:
            stack.append(i)

    cnt = 0
    stack.sort()
    print(stack)
    for i in stack: #k를 이용해서 다시 짜야되 !
        if i+1 in stack:
            # print(i)
            if i+2 in stack:
                print(i)
                break

    if count ==4:
        break

    아항 감사합니디ㅏ
    효율성은 똥이지만 ㅎㅁㅎ





