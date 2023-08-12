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

# 209.
print(solution(["aya", "yee", "u", "maa", "wyeoo"]))