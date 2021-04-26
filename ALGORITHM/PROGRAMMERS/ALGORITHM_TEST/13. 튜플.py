s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"

s = s[2:-2].split('},{')
s = sorted(s, key = lambda x : len(x))
print(s)

answer = []
for i in s:
    ss = i.split(',')
    for j in ss:
        if int(j) not in answer: # int 수치형으로 타입 변환 안한거에서 오래 걸렸다... 백준 폐해....
            answer.append(int(j))
print(answer)


# 차집합으로 풀면 시간 단축 !!
# ss = []
# for i in s:
#     ss.append(list(map(int, i.split(','))))
#
# answer = ss[0]
# for j in range(0, len(ss)-1):
#     answer.extend(list(set(ss[j+1]) - set(ss[j])))
# print(answer)