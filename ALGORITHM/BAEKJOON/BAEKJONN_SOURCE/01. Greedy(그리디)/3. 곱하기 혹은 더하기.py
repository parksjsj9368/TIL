data = input()

result = int(data[0])

for i in range(1, len(data)) :
    if (result <= 1) | (int(data[i]) <= 1) :
        result += int(data[i])
    else :
        result *= int(data[i])

print(result)


# 동빈나씨 코드
#
# data = input()
#
# # 첫 번째 문자를 숫자로 변경하여 대입
# result = int(data[0])
#
# for i in range(1, len(data)) :
#     num = int(data[i])
#     # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기 보다는 더하기 수행
# 	if num <= 1 or result <= 1 :
# 		result += num
# 	else :
# 		result *= num
#
# print(result)