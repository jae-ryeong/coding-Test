# 196. 삼각형의 완성조건 (1)
# def solution(sides):
#     c = max(sides)
#     sides.remove(c)
    
#     if c < sides[0] + sides[1]:
#         return 1
#     else:
#         return 2

# 똑똑하네... 
# return 1 if max(sides) < (sum(sides) - max(sides)) else 2

# 197. 중복된 문자 제거
# def solution(my_string):
#     answer = ''
#     for i in my_string:
#         if i in answer:
#             continue
#         answer += i
#     return answer

# 198. 직사각형 넓이 구하기
# def solution(dots):
#     maxx, maxy = max(dots)
#     minx, miny = min(dots)
#     return (maxx-minx) * (maxy-miny)

# 199. 인덱스 바꾸기
# def solution(my_string, num1, num2):
#     answer= list(my_string)
#     temp = answer[num1]
#     answer[num1] = answer[num2]
#     answer[num2] = temp

#     my_string = ''.join(answer)
     
#     return my_string
# 더 짧게 바꾸기
# s[num1],s[num2] = s[num2],s[num1]
#     return ''.join(s)

# 200. 한 번만 등장한 문자
# def solution(s):
#     check = set(s)
#     check = list(check) * 2

#     for i in s:
#         if i in check:
#             check.remove(i)
    
#     return ''.join(sorted(check))

# count를 사용하자..
#  answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
#     return answer

# 201. 약수 구하기
# def solution(n):
#     return [i for i in range(1,n+1) if n%i==0]

# 202. 머쓱이보다 키 큰 사람
# def solution(array, height):
#     array.append(height)
#     array = sorted(array)
#     return len([i for i in array if i>height])

# 203. 세균 증식
# def solution(n, t):
#     for _ in range(t):
#         n *= 2
#     return n

# 천재
# def solution(n, t):
#     return n << t

# 평범
# def solution(n, t):
#     return n*(2**t)

# 204. 삼각형의 완성조건 (2)
# def solution(sides):
#     answer = 0
#     max_side = max(sides)
#     min_side = min(sides)
    
#     for _ in range(max_side + 1 - min_side, max_side+1):
#         answer+=1
    
#     for _ in range(max_side+1,max_side+min_side):
#         answer+=1
#     return answer

# 천재

# 205. 
print(solution([11, 7]))