# 166. 특정 문자 제거하기
# def solution(my_string, letter):
#     return ''.join([i for i in my_string if not(i in letter)])

# 167. 배열 자르기
# def solution(numbers, num1, num2):
#     return numbers[num1:num2+1]

# 168. 평행
# def solution(dots):
#     case = [[0,1],[2,3],[0,2],[1,3],[0,3],[1,2]]
#     idx1, idx2 = 0, 1

#     for _ in range(3):
#         x1, y1 = abs(dots[case[idx1][0]][0] - dots[case[idx1][1]][0]), abs(dots[case[idx1][0]][1] - dots[case[idx1][1]][1])
#         x2, y2 = abs(dots[case[idx2][0]][0] - dots[case[idx2][1]][0]), abs(dots[case[idx2][0]][1] - dots[case[idx2][1]][1])

#         if x1 / y1 == x2 / y2:
#             return 1

#         idx1+=2
#         idx2+=2
#     return 0
# print(solution([[1,1],[2,2],[3,3],[4,17]]))