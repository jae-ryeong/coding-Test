# 51. 9로 나눈 나머지
# def solution(number):
#     sum=0
#     for i in list(number):
#       sum += int(i)
#     return sum%9

# 52. 주사위 게임 3
# def solution(a, b, c, d):
#     s1 = {a,b,c,d}
#     l1 = list(s1)
#     l2 = sorted([a,b,c,d])
#     if len(s1) == 1:
#         answer = 1111*l1[0]
#     elif len(s1) == 2:
#         if l2.count(l2[0])==3:
#             answer = (10 * l2[0] + l1[1]) ** 2
#         elif l2.count(l2[0])==1:
#             answer = (10 * l2[1] + l1[0]) ** 2
#         elif l2.count(l2[0]) == 2:
#             answer = (l1[0] + l1[1]) * (abs(l1[0] - l1[1]))
#     elif len(s1) == 3:
#         if l2[0] == l2[1]:
#             answer = l2[2] * l2[3]
#         elif l2[1] == l2[2]:
#             answer = l2[0] * l2[3]
#         elif l2[2] == l2[3]:
#             answer = l2[0] * l2[1]
#     else:
#         answer = l1[0]
#     return answer

# 53. 문자열의 뒤의 n글자
# def solution(my_string, n):
#     return my_string[-n:]

# 54. 길이에 따른 연산
# def solution(num_list):
#     if len(num_list) >=11:
#         return sum(num_list)
#     else:
#         return eval('*'.join(str(i) for i in num_list))

# 55. 대문자로 바꾸기
# def solution(myString):
#     return myString.upper()

# 56. 정수 찾기
# def solution(num_list, n):
#     return 1 if n in num_list else 0

# 57. n 번째 원소부터
# def solution(num_list, n):
#     return num_list[n-1:]

# 58. 뒤에서 5등 위로
# def solution(num_list):
#     result = sorted(num_list)
#     return result[5:]
# 한 줄 - return sorted(num_list)[5:]

# 59. 조건에 맞게 수열 변환하기 3
# def solution(arr, k):
#     result = []
#     if k%2:
#         for i in range(len(arr)):
#             result.append(arr[i] * k)
#     else:
#         for i in range(len(arr)):
#             result.append(arr[i] + k)
#     return result
#   한 줄 - return [i*k if k%2!=0 else i+k for i in arr]

# 60. 카운트 다운
# def solution(start, end):
#     return [i for i in range(start, end-1 , -1)]