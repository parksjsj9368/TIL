n = int(input())
h_list = sorted(list(map(int, input().split())))
ans = 10 ** 10

for start in range(n):
    for end in range(start+1, n):

        # 눈사람1 높이
        snowman1 = h_list[start] + h_list[end]  # 눈사람1 높이

        a = start
        b = n - 1

        while True:
            while a == start or a == end:
                a += 1
            while b == start or b == end:
                b -= 1

            if a >= b:
                break

            # 눈사람2 높이
            snowman2 = h_list[a] + h_list[b]
            if snowman1 < snowman2:
                ans = min(ans, snowman2 - snowman1)
                b -= 1
            elif snowman1 >= snowman2:
                ans = min(ans, snowman1 - snowman2)
                a += 1
print(ans)


# 다른 팀원 풀이
#
# n = int(input())
# h_list = sorted(list(map(int, input().split())))
# diff = 10 ** 10
#
# for start in range(n):
#     for end in range(start + 3, n):
#         in_start, in_end = start + 1, end - 1
#
#         while in_start < in_end:
#             tmp_diff = (h_list[start] + h_list[end]) - (h_list[in_start] + h_list[in_end])
#             diff = min(ans, abs(tmp_diff))
#
#             if tmp_diff < 0:
#                 in_end -= 1
#             else:
#                 in_start += 1
# print(diff)
