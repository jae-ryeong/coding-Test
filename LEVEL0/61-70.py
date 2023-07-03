# 61. 문자열 여러 번 뒤집기
# def solution(my_string, queries):
#     my_string = list(my_string)
#     for i in range(len(queries)):
#         s = queries[i][0]
#         e = queries[i][1]
#         while (s<=e):
#             my_string[s], my_string[e] = my_string[e], my_string[s]
#             s+=1
#             e-=1
#     return "".join(my_string)

# for 문장을 이렇게 할 수도 있다.
# my_string = "rermgorpsam"	
# my_string = list(my_string)
# queries = [[2, 3], [0, 7], [5, 9], [6, 10]]	
# for s,e in queries:
#     print(my_string[s:e+1][::-1])
#     my_string[s:e+1]=my_string[s:e+1][::-1]
#     print(my_string)
# print( ''.join(my_string))

# 62. 문자열로 변환
# def solution(n):
#     return str(n)

# 63. 문자열 정수의 합
# def solution(num_str):
#     return eval("+".join(num_str))
# 혹은 - return sum(map(int, list(num_str)))

# 64. 부분 문자열
# def solution(str1, str2):
#     return int(str1 in str2)

# 65. 첫 번째로 나오는 음수
# def solution(num_list):
#     for i in range(len(num_list)):
#         if num_list[i] <0:
#             return i
#     return -1

# 66. 접미사인지 확인하기
# def solution(my_string, is_suffix):
#     for i in range(len(my_string)):
#         if my_string[i:] == is_suffix:
#             return 1
#     return 0
# 좋은 풀이 1. if m[-len(s):]==s: return 1
#             return 0
# 좋은 풀이 2. return int(my_string.endswith(is_suffix))

# 67. 배열 만들기 5
# def solution(intStrs, k, s, l):
#     result,temp = [],[]
#     for i in intStrs:
#         temp = int(str(i[s:s+l]))
#         if temp > k:
#             result.append(temp)
#     return result

# 68. 부분 문자열 이어 붙여 문자열 만들기
# def solution(my_strings, parts):
#     answer = ''
#     for i in range(len(my_strings)):
#         answer += my_strings[i][parts[i][0]:parts[i][1]+1]
#     return answer
#   enumerate 사용 - 
#   for i, (s, e) in enumerate(parts):
#        answer += my_strings[i][s:e+1]

# 69. 접두사인지 확인하기
# def solution(my_string, is_prefix):
#     return 1 if my_string.startswith(is_prefix) else 0

# 70. A 강조하기
# def solution(myString):
#     answer=''
#     for i in myString:
#         if i == 'a' or i == 'A': 
#             answer += i.upper()
#         else: 
#             answer += i.lower()
#     return answer

# 한 줄 - return myString.lower().replace('a', 'A')