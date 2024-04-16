# 21. 문자열 내림차순으로 배치하기
# def solution(s):
#     answer = ''.join(sorted(s)[::-1])
#     return answer

# 22. 문자열 내 p와 y의 개수
# def solution(s):
#     word = s.upper()

#     nump = word.count('P')
#     numy = word.count('Y')

#     if nump == numy: return True
#     else: return False

# 23. 햄버거 만들기
# def solution(ingredient):
#     result = 0
#     s = []
    
#     for i in ingredient:
#         s.append(i)
#         if s[-4:] == [1,2,3,1]:
#             result += 1
#             for _ in range(4):
#                 s.pop()
    
#     return result

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))