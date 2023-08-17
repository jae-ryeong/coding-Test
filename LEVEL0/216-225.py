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

# 220.
print(solution("aAb1B2cCB34oOp"))