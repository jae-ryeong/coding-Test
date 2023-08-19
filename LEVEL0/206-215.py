# 206. 옹알이
# def solution(babbling):
#     words = ["aya", "ye", "woo", "ma"]
#     answer = 0
#     for i in babbling:
#         temp = i
#         for word in words:
#             if word in temp:
#                 temp = temp.replace(word,'*')
        
#         temp = temp.replace('*','')
#         if temp == '': answer+=1
    
#     return answer

# 207. k의 개수
# def solution(i, j, k):
#     li=[]
#     for num in range(i,j+1):
#         for num2 in str(num):
#             li.append(num2)

#     return li.count(str(k))

# 더 괜찮은 답변
# def solution(i, j, k):
#     answer = sum([ str(i).count(str(k)) for i in range(i,j+1)])
#     return answer

# 208. 배열의 유사도
# def solution(s1, s2):
#     answer = 0
#     for check in s1:
#         for check2 in s2:
#             if check == check2:
#                 answer += 1
#     return answer

# 집합으로 표현
# def solution(s1, s2):
#     answer = 0

#     for word in s1:
#         if word in s2:
#             answer += 1
#         else:
#             continue

#     return answer

# 209. 외계어 사전
# def solution(spell, dic):
#     for i in dic:
#         check = 0
#         for j in spell:
#             if j in i:
#                 check+=1
#         if check == len(spell):
#             return 1
#     return 2

# 집합 활용
# def solution(spell, dic):
#     spell = set(spell)
#     for s in dic:
#         if not spell-set(s):
#             return 1
#     return 2

# 210. 잘라서 배열로 저장하기
# def solution(my_str, n):
#     answer = []
#     a=0
#     for i in range(n,len(my_str),n):
#         answer.append(my_str[a:i])
#         a+=n
    
#     if len(my_str) > a:
#         answer.append(my_str[a:])
#     return answer

# 슬라이싱은 초과해도 에러가 나지 않는다 ㅜㅜ
# def solution(my_str, n):
#     return [my_str[i:i+n] for i in range(0,len(my_str),n)]

# 211. 7의 개수
# def solution(array):
#     return sum([str(i).count("7") for i in array])

# 더 쉽게
# def solution(array):
#     return str(array).count('7')

# 212. 이진수 더하기
# def solution(bin1, bin2):
#     answer = int(bin1,2) + int(bin2,2)
#     return bin(answer)[2:]

# 213. 숨어있는 숫자의 덧셈 (2)
# import re
# def solution(my_string):
#     c = re.sub(r"[a-z]"," ",my_string)
#     c = re.sub(r"[A-Z]"," ",c)
#     c = c.strip()

#     return sum(int(i) for i in c.split())

# 깔끔하다
# def solution(my_string):
#     s = ''.join(i if i.isdigit() else ' ' for i in my_string)
#     return sum(int(i) for i in s.split())

# 214. 숫자 찾기
# def solution(num, k):
#     for i in str(num):
#         if int(i) == k:
#             return list(str(num)).index(str(k)) + 1
#     return -1

# enum으로 
# def solution(num, k):
#     for i, n in enumerate(str(num)):
#         if str(k) == n:
#             return i + 1
#     return -1

# 215. 자릿수 더하기
# def solution(n):
#     return sum(int(i) for i in (list(str(n))))