# 101. 1로 만들기
# def solution(num_list):
#     answer = 0
#     for i in range(len(num_list)):
#         while (num_list[i] != 1):
#             if num_list[i] % 2:
#                 num_list[i] = num_list[i]-1
#                 print(num_list[i])
#             num_list[i] /= 2
#             answer+=1
#     return answer

# 102. 배열 비교하기
# def solution(arr1, arr2):
#     if len(arr1) > len(arr2):
#         return 1
#     elif len(arr1) < len(arr2):
#         return -1
#     else:
#         if sum(arr1) == sum(arr2):
#             return 0    
#         elif sum(arr1) > sum(arr2):
#             return 1
#         else:
#             return -1

# 103. 수열과 구간 쿼리 1
# def solution(arr, queries):
#     for j in queries:
#         for i in range(j[0],j[1]+1):
#             arr[i]+=1
#     return arr

# 104. 할 일 목록
# def solution(todo_list, finished):
#     result = []
#     for i,j in enumerate(finished):
#         if j == False:
#             result.append(todo_list[i])
#     return result

# 105. 홀수 vs 짝수
# def solution(num_list):
#     odd,even=0,0
#     for i,j in enumerate(num_list):
#         if (i+1) % 2:
#             odd+=j
#         elif (i+1) %2 == 0:
#             even+=j
#     return odd if odd>even else even
# 개쉽게
# def solution(num_list):
#     return max(sum(num_list[::2]), sum(num_list[1::2]))

# 106. 커피 심부름
# def solution(order):
#     answer = 0
#     for i,j in enumerate(order):
#         if "americano" in j or "anything" in j:
#             answer += 4500
#         else:
#             answer += 5000
#     return answer

# 107. 문자열 묶기
# def solution(strArr):
#     answer = [0] * len(max(strArr,key=len))
#     for j in strArr:
#         answer[len(j)-1] += 1
#     return max(answer)

# 108. 문자열 잘라서 정렬하기
# def solution(myString):
#     answer = []
#     a = myString.split('x')
#     for i in a:
#         if i != '':
#             answer.append(i)
#     return sorted(answer)

# 109. x 사이의 개수
# def solution(myString):
#     answer = []
#     a = myString.split('x')
#     for i in a:
#         answer.append(len(i))
#     return answer
# 한줄코드 return [len(w) for w in myString.split('x')]

# 110. 공백으로 구분하기 2
# def solution(my_string):
#     answer = []
#     for i in my_string.split(' '):
#         if i != '': answer.append(i)
#     return answer 
# 한 줄 ㅜㅜ return my_string.split()