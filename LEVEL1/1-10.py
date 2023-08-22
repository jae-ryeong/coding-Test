# 1. 약수의 합
# def solution(n):
#     answer = 0
#     for i in range(1,n+1):
#         if n%i==0: answer += i
#     return answer

# 2. 하샤드 수
# def solution(x):
#     xsum = sum(int(i) for i in list(str(x)))
#     if x % xsum == 0 : return True
#     return False

# 그냥 이렇게 하면 된다.
# def Harshad(n):
#     return n%sum(int(x) for x in str(n)) == 0

# 3. 정수 내림차순으로 배치하기
# def solution(n):
#     return int(''.join(sorted(str(n), reverse=True)))

# 4. 바탕화면 정리
# def solution(wallpaper):
#     x_index = []
#     y_index = []
#     for i,j in enumerate(wallpaper):
#         if "#" in j:
#             x_index.append(i)
#             y_index.append(j.index("#"))
#             y_index.append(j.rindex("#"))
    
#     y_index.sort()
#     return [x_index[0], y_index[0], x_index[-1]+1, y_index[-1]+1]

# 비슷하지만 더 간단하게
# def solution(wall):
#     a, b = [], []
#     for i in range(len(wall)):
#         for j in range(len(wall[i])):
#             if wall[i][j] == "#":
#                 a.append(i)
#                 b.append(j)
#     return [min(a), min(b), max(a) + 1, max(b) + 1]

# 5. 
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))