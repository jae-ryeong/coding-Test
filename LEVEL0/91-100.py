import re
# 91. 2의 영역
# def solution(arr):
#     answer = []
#     count = []
#     for i,j in enumerate(arr):
#         if j == 2: count.append(i)

#     if len(count)==0:
#         answer.append(-1)
#     elif len(count) == 1:
#         answer.append(2)
#     elif len(count) >= 2:
#         answer += (arr[count[0]:count[-1]+1])
#     return answer

# 내가 하려고 한 코드..
# def solution(arr):
#     if 2 not in arr:
#         return [-1]
#     return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]

# 92. 왼쪽 오른쪽
# def solution(str_list):
#     if 'l' in str_list and 'r' in str_list:
#         if str_list.index('l') > str_list.index('r'):
#             return str_list[str_list.index('r')+1:]
#         elif str_list.index('l') < str_list.index('r'):
#             return str_list[:str_list.index('l')]
#     elif 'l' in str_list:
#         return str_list[:str_list.index('l')]
#     elif 'r' in str_list:
#         return str_list[str_list.index('r')+1:]
#     else:
#         return []

# 훨씬 좋은 방법
# def solution(str_list):
#     for i in range(len(str_list)):
#         if str_list[i]=='l': return str_list[:i]
#         elif str_list[i]=='r': return str_list[i+1:]
#     return []

# 93. 배열의 길이에 따라 다른 연산하기
# def solution(arr, n):
#     if len(arr) %2:
#         for i in range(0,len(arr),2):
#             arr[i] += n
#     else:
#         for i in range(1,len(arr),2):
#             arr[i] += n
#     return arr

# 94. 문자열이 몇 번 등장하는지 세기
# def solution(myString, pat):
#     count2=0
    
#     if(len(pat)==1):
#             return myString.count(pat)
        
#     for i,j in enumerate(myString):
#         count1=0
#         if j == pat[0] and i <= len(myString)-len(pat):
#             for k in range(1,len(pat)):
#                 if myString[i+1] == pat[k]:
#                     i+=1
#                     count1+=1
#                 else:
#                     break
#         if count1 == len(pat)-1:
#             count2 +=1
#     return count2
# 너무 어렵게 풀었다. 다른 사람 풀이를 보면 좋다

# 95. 문자열 바꿔서 찾기
# def solution(myString, pat):
#     answer = []
#     for i in range(len(myString)):
#         if myString[i] == 'A': 
#             answer += 'B'
#         elif myString[i] == 'B':
#             answer += 'A'
    
#     return int(pat in ''.join(answer))

# 96. 날짜 비교하기
# def solution(date1, date2):
#     for i in range(3):
#         if date1[i] > date2[i]: return 0
#         elif date1[i] < date2[i]: return 1
#     return 0
# 개쉽게
# def solution(date1, date2):
#     return int(date1 < date2)

# 97. 배열 만들기 6
# def solution(arr):
#     stk = []
#     i=0
#     while (i<len(arr)):
#         if len(stk) == 0:
#             stk.append(arr[i])
#             i+=1
#         if i >= len(arr): break
#         if stk[-1] == arr[i]:
#             stk.pop()
#             i+=1
#         elif stk[-1] != arr[i]:
#             stk.append(arr[i])
#             i+=1
#     return [-1] if len(stk)==0 else stk

# def solution(arr):
#     stk = []
#     for i in range(len(arr)):
#         if stk and stk[-1] == arr[i]:
#             stk.pop()
#         else:
#             stk.append(arr[i])

#     return stk or [-1]

# 98. 무작위로 K개의 수 뽑기
# def solution(arr, k):
#     answer = []
    
#     for i in range(len(arr)):
#         if arr[i] not in answer: answer.append(arr[i])
#         if(len(answer) == k): return answer
    
#     return answer + [-1] * (k-len(answer))

# 99. 전국 대회 선발 고사
# def solution(rank, attendance):
#     answer = []
    
#     for i in range(len(rank)):
#         if attendance[i] == True:
#             answer.append(rank[i]) 
#     answer = sorted(answer)
#     print(answer)
#     return (10000*rank.index(answer[0])) + (100*rank.index(answer[1])) + rank.index(answer[2])
# def solution(rank, attendance):
#     arr = sorted([(x, i) for i, x in enumerate(rank) if attendance[i]])
#     return arr[0][1] * 10000 + arr[1][1] * 100 + arr[2][1]

# 100. 배열의 원소만큼 추가하기
# def solution(arr):
#     answer = []
#     for j in arr:
#         for k in range(j):
#             answer.append(j)
#     return answer
