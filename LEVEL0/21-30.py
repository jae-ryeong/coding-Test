import math
# 21. n의 배수
# def solution(num, n):
#     return 1 if num%n==0 else 0

# 22. 홀짝에 따라 다른 값 반환하기
# def solution(n):
#     answer = 0
#     odd,even=1,2
#     if n%2:
#         while(odd<=n):
#             answer+=odd
#             odd+=2
#     else:
#         while(even<=n):
#             answer+=(even*even)
#             even+=2
#     return answer

# 23. 조건 문자열
# def solution(ineq, eq, n, m):
#     if ineq == "<":
#         if eq == "=":
#             return(int(n<=m))
#         elif eq=="!":
#             return(int(n<m))
#     elif ineq == ">":
#         if eq == "=":
#             return(int(n>=m))
#         elif eq=="!":
#             return(int(n>m))
#     한줄로 - return int(eval(str(n)+ineq+eq.replace('!', '')+str(m))) *eval ex) ("1+2") = 3

# 24. flag에 따라 다른 값 반환하기
# def solution(a, b, flag):
#     return a+b if flag else a-b

# 25. 코드 처리하기
# def solution(code):
#     mode=0
#     ret=""
#     for i in range(len(code)):
#         if mode==0:
#             if code[i] != "1":
#                 if i%2==0:
#                     ret+=code[i]
#             elif code[i] == "1":
#                 mode=1  
#         else:
#             if code[i]=="1":
#                 mode=0
#             else:
#                 if i%2:
#                     ret+=code[i]
#     return "EMPTY" if ret=="" else ret
#     엄청 쉽게 - return "".join(code.split("1"))[::2] or "EMPTY"

# 26. 등차수열의 특정한 항만 더하기
# def solution(a, d, included):
#     answer=0
#     for i in range(len(included)):
#         if included[i]:
#             answer += a + d*(i)
#         answer += (a + d * i) * int(included[i]) - if문 없이
#     return answer

# 27. 주사위 게임2
# def solution(a, b, c):
#     if a != b and a != c and b != c:
#         return a+b+c
#     elif a == b == c:
#         return (a+b+c) * (a*a+b*b+c*c) * (a**3+b**3+c**3)
#     elif a==b or a==c or b==c:
#         return (a+b+c) * (a*a+b*b+c*c)

# def solution(a, b, c):  # 참신한거
#     check=len(set([a,b,c]))
#     if check==1:
#         return 3*a*3*(a**2)*3*(a**3)
#     elif check==2:
#         return (a+b+c)*(a**2+b**2+c**2)
#     else:
#         return (a+b+c)

# 28. 원소들의 곱과 합
# def solution(num_list):
#     answer = 1
#     for i in num_list:
#         answer *= i
#     return 1 if sum(num_list)**2 > answer else 0

# def solution(num_list): # 내가 구상한 코드
#     s=sum(num_list)**2
#     m=eval('*'.join([str(n) for n in num_list]))
#     return 1 if s>m else 0

# def solution(num_list): # bool -> int return
#     mul = 1 
#     for n in num_list:
#         mul *= n
#     return int(mul < sum(num_list) ** 2)

# 29. 이어 붙인 수
# def solution(num_list): # 시간 복잡도가 2배이다, 기본 코드로 짜는게 더 낫다..
#     odd = int(''.join([str(i) for i in num_list if i%2]))
#     even = int(''.join([str(i) for i in num_list if i%2==0]))
#     return odd+even

# 30. 마지막 두 원소
# def solution(num_list):
#     if num_list[-2] < num_list[-1]:
#         num_list.append(num_list[-1] - num_list[-2])
#     else:
#         num_list.append(num_list[-1]*2)
#     return num_list

# def solution(l): # 코드를 짧게
#     l.append(l[-1]-l[-2] if l[-1]>l[-2] else l[-1]*2)
#     return l