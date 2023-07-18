# 156. 직각삼각형 출력하기
# n = int(input())
# for i in range(n):
#     star = ""
#     for _ in range(i+1):
#         star += "*"
#     print(star)

# 157. 짝수 홀수 개수
# def solution(num_list):
#     answer = [0,0]
#     for i in num_list:
#         if i%2:
#             answer[1] += 1
#         else:
#             answer[0] +=1
#     return answer
# 좋은 센스: answer[n%2]+=1

# 158. 겹치는 선분의 길이   - 못 풀었다.
# def solution(lines):
#     line_list = []
#     for line in lines:
#         line_list += line
#     mx, mn = max(line_list), min(line_list)

#     x, y, z = lines
#     print(f"x={x}, {y}, {z}")
#     overlap_line_count = 0
#     for i in range(mn, mx+1):
#         overlap_point_count = 0

#         if x[0] <= i < x[1]:
#             overlap_point_count += 1
#         if y[0] <= i < y[1]:
#             overlap_point_count += 1
#         if z[0] <= i < z[1]:
#             overlap_point_count += 1

#         if overlap_point_count >= 2:
#             overlap_line_count += 1
#         print(f'i x y z overlap_point_count overlap_line_count', i, x, y, z, overlap_point_count, overlap_line_count)

#     return overlap_line_count
# 굉장한 답변
# sets = [set(range(min(l), max(l))) for l in lines]
#     return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])

# 159.