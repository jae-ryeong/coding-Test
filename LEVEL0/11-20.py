# 11. 문자열 섞기
# def solution(str1, str2):
#     answer = ''
#     for i in range(len(str1)):
#         answer += str1[i] + str2[i]
#     return answer

# 12. 문자 리스트를 문자열로 변환하기
# arr = ["a","b","c"]
# result=''
# for i in arr:
#     result+=i

# print(result)
# return ''.join(arr) - 쉽게 하는법

# 13. 문자열 곱하기
# def solution(my_string, k):
#     return my_string*k

# 14. 더 크게 합치기
# def solution(a, b):
#     return int(str(a)+str(b)) if int(str(a)+str(b))>=int(str(b)+str(a)) else int(str(b)+str(a)) 
#     쉽게 - return int(max(f"{a}{b}", f"{b}{a}"))

# 15. 두 수의 연산값 비교하기
# def solution(a, b):
#     c = int(str(a)+str(b))
#     d = 2*a*b
#     return (c if c>=d else d)
# 쉽게 - return max(int(str(a) + str(b)), 2 * a * b)

# 16. n개 간격의 원소들
# def solution(num_list, n):
#     if n<1 and n>4:
#         n = input()
        
#     k=0
#     answer = []
    
#     while(k < len(num_list)):
#         answer.append(num_list[k])
#         k+=n
#     return answer

#     쉽게 - return num_list[::n]

# 17. 문자열을 정수로 변환하기
# def solution(n_str):
#     return int(n_str)

# 18. 공배수
# def solution(number, n, m):
#     answer = 0
#     if number%n==0 and number%m==0:
#         answer=1
#     else:
#         answer=0
#     return answer

#     return int(bool(number % n == 0) & bool(number % m == 0)) - bool을 이용한 return

# 19. 문자열의 앞의 n글자
def solution(my_string, n):
    return my_string[:n]

# 20. 조건에 맞게 수열 변환하기 1
# def solution(arr):
#     answer = []
#     for i in arr:
#         if i >=50 and i%2 == 0:
#             answer.append(i/2)
#         elif i<50 and i%2==1:
#             answer.append(i*2)
#         else:
#             answer.append(i)
#     return answer

# 한줄로 표현 - return [num/2 if num>=50 and num%2==0 else (num*2 if num<50 and num%2==1 else num) for num in arr]