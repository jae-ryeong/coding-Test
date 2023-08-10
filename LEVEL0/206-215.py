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

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))