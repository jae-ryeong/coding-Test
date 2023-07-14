# 126. 몫 구하기
# def solution(num1, num2):
#     return num1 // num2

# 127. 두 수의 합
# def solution(num1, num2):
#     return num1 + num2

# 128. 두 수의 곱
# solution = lambda num1, num2 : num1 * num2

# 129. 두 수의 차
# solution = lambda num1, num2 : num1 - num2

# 130. 분수의 덧셈
# def solution(numer1, denom1, numer2, denom2):
#     answer = []
#     numer1 *= denom2
#     numer2 *= denom1
#     denom1 *= denom2
#     denom2 = denom1
    
#     numer3 = numer1 + numer2

#     i=2
#     count = max(numer3,denom2) // 2
#     while (i <= count):
#         if numer3%i == 0 and denom2%i == 0:
#             numer3 = numer3//i
#             denom2 = denom2//i
#             i=2
#         else: i+=1
#     answer.append(numer3)
#     answer.append(denom2)
#     return answer

# math 함수 적용
# import math

# def solution(denum1, num1, denum2, num2):
#     denum = denum1 * num2 + denum2 * num1
#     num = num1 * num2
#     gcd = math.gcd(denum, num)
#     return [denum//gcd, num//gcd]

# 131. 숫자 비교하기
# def solution(num1, num2):
#     return 1 if num1 == num2 else -1

# 132. 나머지 구하기
# def solution(num1, num2):
#     return num1%num2

# 133. 나이 출력
# def solution(age):
#     return 2022 - age + 1

# 134. 중복된 숫자 개수
# def solution(array, n):
#     return array.count(n)

# 135. 컨트롤 제트
# def solution(s):
#     s= s.split(" ")
#     sum = ""
#     for i in range(len(s)):
#         if s[i] == "Z":
#             sum += "-"+s[i-1]
#         else:
#             sum += "+"+s[i]
#     return eval(sum)
# 다른 풀이
# def solution(s):
#     stack = []
#     for a in s.split():
#         if a != 'Z':
#             stack.append(int(a))
#         else:
#             if stack:
#                 stack.pop()

#     return sum(stack)