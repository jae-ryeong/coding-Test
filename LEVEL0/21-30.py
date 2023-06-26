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
code="abc1abc1abc"
mode=0
ret=""
for i in range(len(code)):
    if mode==0:
        if code[i]==1:
            mode=1
        else:
            if i%2==0: 
                ret+=code[i]    
    else:
        if code[i]==1:
            mode=0
        else:
            if i%2:
                ret+=code[i]
print(ret)
        


