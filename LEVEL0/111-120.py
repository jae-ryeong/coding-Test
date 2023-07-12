# 111. 뒤에서 5등까지
# def solution(num_list):
#     return sorted(num_list)[:5]

# 112. 0 떼기
# def solution(n_str):
#     return n_str.lstrip('0')

# 113. l로 만들기
# def solution(myString):
#     answer = ''
#     for i in myString:
#         if ord(i) < 108:
#             answer += 'l'
#         else: answer += i
#     return answer
# 한 줄 풀이
# return myString.translate(str.maketrans('abcdefghijk', 'lllllllllll'))

# 114. 그림 확대 - 해석보기
# def solution(picture, k):
#     answer = []
#     for i in picture:
#         str = ''

#         for j in i:
#             str += j * k
#         for _ in range(k):
#             answer.append(str)

#     return answer

# 115. 배열의 원소 삭제하기
# def solution(arr, delete_list):
#     answer=[]
#     answer += arr
#     for i in arr:
#         for j in delete_list:
#             if i == j:
#                 answer.remove(i)
#                 break
#     return answer 
# 한 줄 코드
#return [i for i in arr if i not in delete_list]

# 116. 특별한 이차원 배열 2
# def solution(arr):
#     for i,result in enumerate(arr):
#         for j in range(len(result)):
#             if arr[i][j] != arr[j][i]:
#                 return 0
#     return 1

# 117. ad 제거하기
# def solution(strArr):
#     return [i for i in strArr if "ad" not in i]

# 118. 간단한 식 계산하기
# def solution(binomial):
#     return int(eval(binomial))

# 119. 세 개의 구분자
# def solution(myStr):
#     answer = []
#     myStr = (myStr.replace('a',' ').replace('b',' ').replace('c',' '))
#     myStr = (myStr.split(" "))
#     for i in myStr:
#         if i != '':
#             answer.append(i)
#     return answer

# 120. 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기
# def solution(myString, pat):
#     answer = ''
#     myString = myString[::-1]
#     pat = pat[::-1]
#     for i in range(myString.index(pat),len(myString)):
#         answer+= myString[i]
#     return answer[::-1]
# 다른 풀이
# solution=lambda x,y:x[:x.rindex(y)+len(y)]
# print(solution("AAAAaaaa","a"))
# print("AAAAaaaa".rindex('a'))