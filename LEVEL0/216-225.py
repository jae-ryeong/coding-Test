# 216. A로 B 만들기
# def solution(before, after):
#     after = list(after)
#     for i in before:
#         if i in after:
#             after.remove(i)
#         else:
#             return 0
#     return 1
            
# 엄청난 정답
# def solution(before, after):
#     before=sorted(before)
#     after=sorted(after)
#     if before==after:
#         return 1
#     else:
#         return 0

# 217. 가장 큰 수 찾기
# def solution(array):
#     answer = [max(array)]
#     answer.append(array.index(answer[0]))
#     return answer

# def solution(array):
#     return [max(array), array.index(max(array))]

# 218. 문자열안에 문자열
# def solution(str1, str2):
#     return 1 if str2 in str1 else 2

# 219. 제곱수 판별하기
# import math
# def solution(n):
#     return 1 if math.sqrt(n) % 1 == 0 else 2

# def solution(n):
#     return 1 if (n ** 0.5).is_integer() else 2

# 220. n의 배수 고르기
# def solution(n, numlist):
#     return [i for i in numlist if i%n==0]

# 221. 최댓값 만들기 (2)
# def solution(numbers):
#     numbers = sorted(numbers)
#     a = numbers[0] * numbers[1]
#     b = numbers[-1] * numbers[-2]
#     return max(a,b)

# 222. 가까운 수
# def solution(array, n):
#     temp = [abs(i-n) for i in array]
#     temp = sorted(temp)
#     return -temp[0]+n if -temp[0]+n in array else temp[0]+n

# 223. 
print(solution([3, 10, 12, 28],20))