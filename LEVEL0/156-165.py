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

# 159. 양꼬치
# def solution(n, k):
#     return (12000 * n) + (2000 * (k - n//10))

# 160. 문자열 밀기
# def solution(A, B):
#     answer = 0
#     for i in range(len(A)):
#         if A==B:
#             return answer
#         A = A[-1] + A[:len(A)-1]
#         answer+=1
#     return -1

# 한 줄 풀이    - solution=lambda a,b:(b*2).find(a)

# 161. 짝수의 합
# solution=lambda n: sum(i for i in range(2,n+1, 2))

# 162. 유한소수 판별하기
# def solution(a, b):
#     point = min(a,b) // 2
#     n = 2
#     while(n <= point):
#         if a%n == 0 and b%n == 0:
#             a = a//n
#             b = b//n
#             n=2
#         n+=1
#     print(b)
#     for _ in range(b//2):
#         if b in (1, 2, 4, 5, 8):
#             return 1
#         elif b in (3, 6, 7, 9):
#             return 2
        
#         if b%2 == 0:
#             b = b//2
#         elif b%5 == 0:
#             b = b//5
#         else:
#             return 2     
    
#     return 1
# print(solution(15,22))

# 163. 각도기
# def solution(angle):
#     if angle > 0 and angle <90:
#         return 1
#     elif angle == 90:
#         return 2
#     elif angle > 90 and angle < 180:
#         return 3
#     else:
#         return 4

# 164. 종이 자르기
# def solution(M, N):    
#     return (M) * (N-1) + (M-1)

# 165. 모음 제거
# def solution(my_string):
#     return my_string.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
# 한 줄 코드 - return "".join([i for i in my_string if not(i in "aeiou")])