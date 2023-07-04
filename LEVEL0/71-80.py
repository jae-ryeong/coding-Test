# 71. n보다 커질 때까지 더하기
# def solution(numbers, n):
#     sum = 0
#     for i in numbers:
#         sum+=i
#         if sum>n: break
#     return sum

# 72. 특정한 문자를 대문자로 바꾸기
# def solution(my_string, alp):
#     return my_string.replace(alp, alp.upper())

# 73. 원하는 문자열 찾기
# def solution(myString, pat):
#     return 1 if pat.lower() in myString.lower() else 0

# 74. 공백으로 구분하기 1
# def solution(my_string):
#     return my_string.split(" ")

# 75. 배열에서 문자열 대소문자 변환하기
# def solution(strArr):
#     for i in range(len(strArr)):
#         if i%2:
#             strArr[i] = strArr[i].upper()
#         else:
#             strArr[i] = strArr[i].lower()
#     return strArr

# 76. 조건에 맞게 수열 변환하기 2
# def solution(arr):
#     result = 0
#     while (True):
#         stop = []
#         stop.extend(arr)
#         for i,j in enumerate(arr):
#             if j>=50 and j%2==0:
#                 arr[i] = j/2
#             elif j<50 and j%2==1:
#                 arr[i] = j*2 + 1
#         if stop == arr:
#             break
#         result+=1
#     return result

# 77. 부분 문자열인지 확인하기
# def solution(my_string, target):
#     return int(target in my_string)

# 78. 꼬리 문자열
# def solution(str_list, ex):
#     answer = ''
#     for i,j in enumerate(str_list):
#         if ex not in j:
#             answer+=j
#     return answer

# 79. 문자열 뒤집기
# def solution(my_string, s, e):
#     return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]

# 80. 배열의 길이를 2의 거듭제곱으로 만들기
# def solution(arr):
#     a=1
#     while (True):
#         if len(arr) <= a:
#             break
#         a *= 2
#     while (len(arr) < a):
#         arr.append(0)
#     return arr