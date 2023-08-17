# 216. A로 B 만들기
# def solution(before, after):
#     after = list(after)
#     for i in before:
#         if i in after:
#             after.remove(i)
#         else:
#             return 0
#     return 1
            
# 엄청난 정답
# def solution(before, after):
#     before=sorted(before)
#     after=sorted(after)
#     if before==after:
#         return 1
#     else:
#         return 0

# 217. 

print(solution("aAb1B2cCB34oOp"))