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

# 5. 자릿수 더하기
# def solution(n):
#     return sum(int(i) for i in str(n))

# 6. 제일 작은 수 제거하기
# def solution(arr):
#     min_arr = min(arr)
#     if len(arr) == 1:
#         return [-1]    
#     return [i for i in arr if i!=min_arr]
# 변수를 사용하지 않으면 시간복잡도가 증가해 에러가 난다. 왜인지 모름

# 7. 둘만의 암호
# def solution(s, skip, index):
#     answer = []
#     skip_ord = [ord(i) for i in skip]
    
#     for i in s:
#         check_ord = ord(i)
#         for _ in range(index):
#             check_ord = check_ord + 1
#             if check_ord > 122: check_ord = check_ord-26
#             while(check_ord in skip_ord):
#                 check_ord = check_ord + 1
#                 if check_ord > 122: check_ord = check_ord-26
#             if check_ord > 122: check_ord = check_ord-26
#         answer.append(chr(check_ord))    

#     return ''.join(answer)

# from string import ascii_lowercase

# def solution(s, skip, index):
#     result = ''

#     a_to_z = set(ascii_lowercase)
#     a_to_z -= set(skip)
#     a_to_z = sorted(a_to_z)
#     l = len(a_to_z)

#     dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}

#     for i in s:
#         result += a_to_z[(dic_alpha[i] + index) % l]

#     return result
print(solution("y", "baz", 1))