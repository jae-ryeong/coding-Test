# 186. 연속된 수의 합 (틀림), (못 풀음)
# def solution(num, total):
#     ave = total // num
#     return [i for i in range(ave - (num-1)//2, ave + (num + 2)//2)]

# 187. 팩토리얼
# def solution(n):
#     answer = 1
#     num = 1
#     while (True):
#         answer *= num
#         if answer > n:
#             num-=1
#             break
#         num += 1
#     return num

# 188. 주사위의 개수
# def solution(box, n):
#     x = box[0] // n
#     y = box[1] // n
#     z = box[2] // n
#     return x * y * z

# 189. 안전지대
# def solution(board):
#     answer = 0

#     for i,j in enumerate(board):
#         for k in j:
#             if k == 1:
#                 check_indexK = (j.index(k))
#                 board[i][check_indexK] = 2 # index(k)를 동작시키기위해

#                 if check_indexK > 0:
#                     if board[i][check_indexK-1] != 1: board[i][check_indexK-1] = 2 # 1 왼쪽을 2로 바꿔준다.

#                 if check_indexK < len(j)-1:
#                         if board[i][check_indexK+1] != 1: board[i][check_indexK+1] = 2 # 1 오른쪽을 2로 바꿔준다.

#                 if len(board)-1 > i:  # 1 아래 구역
#                     if board[i+1][check_indexK] != 1: board[i+1][check_indexK] = 2  # 1 아래를 2로 바꿔준다
                    
#                     if check_indexK > 0: 
#                         if board[i+1][check_indexK-1] != 1: board[i+1][check_indexK-1] = 2 # 1 아래 왼쪽을 2로 바꿔준다.
                    
#                     if check_indexK < len(j)-1:
#                         if board[i+1][check_indexK+1] != 1: board[i+1][check_indexK+1] = 2 # 1 아래 오른쪽을 2로 바꿔준다.
                
#                 if i != 0:  # 1 위쪽에 배열이 있다면
#                     if board[i-1][check_indexK] != 1: board[i-1][check_indexK] = 2  # 1 위를 2로 바꿔준다

#                     if check_indexK > 0: 
#                         if board[i-1][check_indexK-1] != 1: board[i-1][check_indexK-1] = 2 # 1 위 왼쪽을 2로 바꿔준다.
                    
#                     if check_indexK < len(j)-1:
#                         if board[i-1][check_indexK+1] != 1: board[i-1][check_indexK+1] = 2 # 1 위 오른쪽을 2로 바꿔준다.

#     for i in board:
#         for j in i:
#             if j == 0 : answer += 1
#     return answer

# 190. 
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))