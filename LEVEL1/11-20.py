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

#14. 수박수박수박수박수박수?
# def solution(n):
#     answer = ''
    
#     if n%2 == 0:
#         answer += '수박' * (n//2)
#     else:
#         answer += '수박' * (n//2) + '수'
    
#     return answer

# 좋은 코드
# str = "수박"*n
#     return str[:n]

#15. 두 정수 사이의 합
# def solution(a, b):
#     sum = 0
#     for i in range(min(a,b), max(a,b)+1):
#         sum += i
#     return sum

# 수학적 지식
# def adder(a, b):
#     return (abs(a-b)+1)*(a+b)//2

#16. 제일 작은 수 제거하기
# def solution(arr):
#     if len(arr) == 1:
#         return [-1]
#     answer = arr.remove(min(arr))
#     return [i for i in arr if i != min(arr)]

#17. 정수 제곱근 판별
# def solution(n):
#     sqrt = n**0.5
#     if (int(sqrt) == sqrt):
#         return (sqrt+1) ** 2
#     else:
#         return -1

#18. 키패드 누르기
# def solution(numbers, hand):
#     answer = ''
#     phone = {
#         1:[0,0], 2:[0,1], 3:[0,2],
#         4:[1,0], 5:[1,1], 6:[1,2],
#         7:[2,0], 8:[2,1], 9:[2,2],
#         '*':[3,0], 0:[3,1], '#':[3,2]
#     }
#     LTemp = '*'
#     RTemp = '#'
#     hh = hand[0:1].upper()
#     for i in numbers:
#         if i in [1,4,7]:
#             LTemp = i
#             answer+='L'
#         elif i in [3,6,9]:
#             RTemp = i
#             answer+='R'
#         else:
#             CArr = phone.get(i)

#             LArr = phone.get(LTemp)
#             RArr = phone.get(RTemp)

#             LPoint = abs(CArr[0] - LArr[0]) + abs(CArr[1] - LArr[1])
#             RPoint = abs(CArr[0] - RArr[0]) + abs(CArr[1] - RArr[1])

#             if LPoint < RPoint:
#                 answer += 'L'
#                 LTemp = i
#             elif LPoint > RPoint:
#                 answer += 'R'
#                 RTemp = i
#             else:
#                 answer += hh
#                 if hh == 'L':
#                     LTemp = i
#                 else:
#                     RTemp = i
#     return answer
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))