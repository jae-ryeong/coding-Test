# 11. x만큼 간격이 있는 n개의 숫자
# def solution(x, n):
#     if x == 0:
#         return [0] * n
#     return [i for i in range(x,x*(n+1),x)]

#12. 짝수와 홀수
# def solution(num):
#     return "Odd" if num%2 else "Even"

#13. 실패율
# def solution(N, stages):
#     challengerPlayer = len(stages)
#     n_stage = {}

#     for i in range(N):
#         if challengerPlayer != 0:
#             n_stage[i+1] = stages.count(i+1)/challengerPlayer
#             challengerPlayer -= stages.count(i+1)
#         else:
#             n_stage[i+1] = 0

#     return sorted(n_stage, key=lambda x:n_stage[x], reverse=True)

# def solution(N, stages): # 훨씬 효율적이고 빠른 코드이다.
#     answer = []
#     fail = []
#     info = [0] * (N + 2)
#     for stage in stages:
#         info[stage] += 1
#     for i in range(N):
#         be = sum(info[(i + 1):])
#         yet = info[i + 1]
#         if be == 0:
#             fail.append((str(i + 1), 0))
#         else:
#             fail.append((str(i + 1), yet / be))
#     print(fail)
#     for item in sorted(fail, key=lambda x: x[1], reverse=True):
#         answer.append(int(item[0]))
#     return answer

#14. 
print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))