## 예를 들어 mylist [[1, 2, 3], [4, 5, 6], [7, 8, 9]]가 주어진 경우,
## solution 함수는 [[1, 4, 7], [2, 5, 8], [3, 6, 9]] 을 리턴하면 됩니다.

mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
answer = [[] for _ in range(len(mylist))]
for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        answer[i].append(mylist[j][i])
print(answer)


# zip 함수 : 각 객체가 담고 있는 원소를 튜플의 형대로 접근
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))
print(new_list)
