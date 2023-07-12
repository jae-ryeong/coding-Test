# 121. 특별한 이차원 배열 1
# def solution(n):
#     answer = [[0 for i in range(n)] for j in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 answer[i][j] = 1
#             else:
#                 answer[i][j] = 0
#     return answer
# def solution(n):
#     answer=[[0]*n for i in range(n)]
#     for i in range(n): answer[i][i]=1
#     return answer
#[[0]*n]*n 형식으로 2차원 배열을 선언하면 얕은 복사가 이루어져 [0][0]=1이 되면 [1][0]=1,[2][0]=1...[n-1][0]=1 이 됩니다.
#이걸 막으려면 [[0 for i in range(n)] for j in range(n)] 형식으로 선언하면 된다고 하네요.

# 122. 이차원 배열 대각선 순회하기
# def solution(board, k):
#     answer = 0
#     for i in range(len(board)):
#         print(i)
#         for j in range(len(board[i])):
#             print(j)
#             if i + j <= k:
#                 answer += board[i][j]
#     return answer

# 123. 빈 배열에 추가, 삭제하기
# def solution(arr, flag):
#     answer = []
#     for i in range(len(arr)):
#         if flag[i] == True:
#             for _ in range(arr[i]*2):
#                 answer.append(arr[i])
#         elif flag[i] == False and len(answer)!=0:
#             for _ in range(arr[i]):
#                 answer.pop()
#     return answer


# 124. 정수를 나선형으로 배치하기
# def solution(n):
#     answer = [[0 for j in range(n)] for i in range(n)]
#     x, y = 0, 0
#     num = 1
#     dir ='r'

#     if n == 1:
#         return [1]
    
#     while(num <= n*n):
#         answer[x][y]=num
#         num+=1
#         if dir == 'r':
#             y+=1
#             if y == n-1 or answer[x][y+1] != 0:
#                 dir = 'd'
#         elif dir == 'd':
#             x+=1
#             if x >= n-1 or answer[x+1][y] != 0:
#                 dir = 'l'
#         elif dir == 'l':
#             y -= 1
#             if y == 0 or answer[x][y-1] != 0:
#                 dir='u'
#         elif dir == 'u':
#             x -= 1
#             if answer[x-1][y] != 0:
#                 dir='r'
#     return answer