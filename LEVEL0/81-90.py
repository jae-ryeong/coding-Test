# 81. 배열 조각하기
# def solution(arr, query):
#     for i in range(len(query)):
#         if i%2:
#             for k in range(query[i]):
#                 arr.pop(0)
#         else:
#             for k in range(len(arr)-query[i]-1):
#                 arr.pop(query[i]+1)
#     return arr

# 쉬운풀이 -
#     for k, q in enumerate(query):
#         if k % 2 == 0:
#             arr = arr[:q + 1]
#         else:
#             arr = arr[q:]
#     return arr

# 82. qr code
# def solution(q, r, code):
#     answer = ''
#     for i, j in enumerate(code):
#         if i%q == r:
#             answer+=j
#     return answer
# 한줄 return code[r::q]

# 83. 세로 읽기
# def solution(my_string, m, c):
#     answer = []
#     answer+=(i for i in my_string)
#     return ''.join(answer[c-1::m])

# 84. 5명씩
# def solution(names):
#     return names[::5]

# 85. 가까운 1 찾기
# def solution(names):
#     return names[::5]
# 다른풀이
# def solution(arr, idx):
#     answer = 0
#     try:
#         answer = arr.index(1, idx)
#     except:
#         answer = -1
#     return answer

# 86. 문자 개수 세기
# def solution(my_string):
#     answer = []
#     for i in range(52):
#         answer.append(0)
#     for i in my_string:
#         if i=='A': answer[0]+=1
#         if i=='B': answer[1]+=1
#         if i=='C': answer[2]+=1
#         if i=='D': answer[3]+=1
#         if i=='E': answer[4]+=1
#         if i=='F': answer[5]+=1
#         if i=='G': answer[6]+=1
#         if i=='H': answer[7]+=1
#         if i=='I': answer[8]+=1
#         if i=='J': answer[9]+=1
#         if i=='K': answer[10]+=1
#         if i=='L': answer[11]+=1
#         if i=='M': answer[12]+=1
#         if i=='N': answer[13]+=1
#         if i=='O': answer[14]+=1
#         if i=='P': answer[15]+=1
#         if i=='Q': answer[16]+=1
#         if i=='R': answer[17]+=1
#         if i=='S': answer[18]+=1
#         if i=='T': answer[19]+=1
#         if i=='U': answer[20]+=1
#         if i=='V': answer[21]+=1
#         if i=='W': answer[22]+=1
#         if i=='X': answer[23]+=1
#         if i=='Y': answer[24]+=1
#         if i=='Z': answer[25]+=1
#         if i=='a': answer[26]+=1
#         if i=='b': answer[27]+=1
#         if i=='c': answer[28]+=1
#         if i=='d': answer[29]+=1
#         if i=='e': answer[30]+=1
#         if i=='f': answer[31]+=1
#         if i=='g': answer[32]+=1
#         if i=='h': answer[33]+=1
#         if i=='i': answer[34]+=1
#         if i=='j': answer[35]+=1
#         if i=='k': answer[36]+=1
#         if i=='l': answer[37]+=1
#         if i=='m': answer[38]+=1
#         if i=='n': answer[39]+=1
#         if i=='o': answer[40]+=1
#         if i=='p': answer[41]+=1
#         if i=='q': answer[42]+=1
#         if i=='r': answer[43]+=1
#         if i=='s': answer[44]+=1
#         if i=='t': answer[45]+=1
#         if i=='u': answer[46]+=1
#         if i=='v': answer[47]+=1
#         if i=='w': answer[48]+=1
#         if i=='x': answer[49]+=1
#         if i=='y': answer[50]+=1
#         if i=='z': answer[51]+=1
#     return answer
    # def solution(my_string):
    # answer=[0]*52
    # for x in my_string:
    #     if x.isupper():
    #         answer[ord(x)-65]+=1
    #     else:
    #         answer[ord(x)-71]+=1
    # return answer (제대로 된 답)

# 한줄 괜찮은 답 - def solution(my_string):
#   return [my_string.count(alphabet) for alphabet in 'abcdefghijklmnopqrstuvwxyz'.upper()+'abcdefghijklmnopqrstuvwxyz']

# 87. 글자 지우기
# def solution(my_string, indices):
#     indices.sort(reverse=True)
#     my_string = list(my_string)
#     for i in indices:
#         my_string.pop(i)
#     return ''.join(my_string)

# 괜찮다
# def solution(my_string, indices):
#     answer = ''
#     for i in range(len(my_string)):
#         if i not in indices:answer+=my_string[i]
#     return answer

# 88. 순서 바꾸기
# def solution(num_list, n):
#     return num_list[n:] + num_list[:n]

# 89. 배열 만들기3
# def solution(arr, intervals):
#     answer=[]
#     for i,j in enumerate(intervals):
#         answer+=arr[j[0]:j[1]+1]
#     return answer

# 90. 리스트 자르기
# def solution(n, slicer, num_list):
#     answer = []
#     if n == 1:
#         answer += num_list[:slicer[1]+1]
#     elif n == 2:
#         answer += num_list[slicer[0]:]
#     elif n == 3:
#         answer += num_list[slicer[0]:slicer[1]+1]
#     elif n == 4:
#         answer += num_list[slicer[0]:slicer[1]+1:slicer[2]]
#     return answer