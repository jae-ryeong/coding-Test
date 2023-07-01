# 51. 9로 나눈 나머지
# def solution(number):
#     sum=0
#     for i in list(number):
#       sum += int(i)
#     return sum%9

# 52. 주사위 게임 3

# s1 = {a,b,c,d}
# l1 = list(s1)
# l2 = sorted([a,b,c,d])
# if len(s1) == 1:
#     answer = 1111*a
# elif len(s1) == 2:
#     if l2[0] == l2[2]:
#         answer = (10 * l1[0] + l1[1]) ** 2
#     else:
#         answer = (s1[0] + s1[1]) * (abs(s1[0] - s1[1]))
# elif len(s1) == 3:
#     answer = l2[1] * l2[2]
# else:
#     answer = l1[0]

# def solution(a, b, c, d):
#     s1 = {a,b,c,d}
#     l1 = list(s1)
#     l2 = sorted([a,b,c,d])
#     if len(s1) == 1: # 완벽
#         answer = 1111*a
#     elif len(s1) == 2:
#         if l2.count(l2[0])==3:
#             answer = (10 * l2[0] + l1[1]) ** 2
#         elif l2.count(l2[0])==1:
#             answer = (10 * l2[1] + l1[0]) ** 2
#         elif l2.count(l2[0]) == 2:
#             answer = (l1[0] + l1[1]) * (abs(l1[0] - l1[1]))
#     elif len(s1) == 3:
#         answer = l1[1] * l1[2]
#     else:
#         answer = l1[0]
#     print(s1)
#     print(l1)
#     print(l2)
#     return answer
# print(solution(2,6,4,5))    # 안되는 반례 (1,1,4,1)

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