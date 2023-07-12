# 136. 두 수의 나눗셈
# def solution(num1, num2):
#     return int(num1 / num2 * 1000)

# 137. 배열 두 배 만들기
# def solution(numbers):
#     answer = []
#     for i in numbers:
#         answer.append(i*2)
#     return answer
# 한 줄 코드1:
# return [num*2 for num in numbers]
# 한 줄 코드2:
# return list(map(lambda x: x * 2, numbers))

# 138. 중앙값 구하기
# def solution(array):
#     array = sorted(array)
#     return array[len(array)//2]

# 139. OX퀴즈
# def solution(quiz):
#     result = []
#     for i in quiz:
#         i = i.replace(' ','')
#         answer = ""

#         answer=i.split("=")
#         num = eval(answer[0])

#         if num == int(answer[1]):
#             result.append("O")
#         else:
#             result.append("X")
#     return result

# 140. 최빈값 구하기
# def solution(array):
#     array_count=[0 for i in range(max(array))] +[0]
    
#     for i in array:
#         array_count[i] += 1
    
#     if array_count.count(max(array_count)) >= 2:
#         return -1
    
#     return array_count.index(max(array_count))

# 141. 짝수는 싫어요.
# def solution(n):
#     return [i for i in range(n+1) if i%2]

# 142. 피자 나눠 먹기 (1)
# def solution(n):
#     return n//7+1 if n%7 else n//7
# 더 좋은 풀이
# return (n+6) // 7

# 143. 피자 나눠 먹기 (2)
# def solution(n):
#     answer = 1
#     number = 6
#     while (True):
#         if number%n == 0:
#             return answer
#         elif number%n != 0:
#             number+=6
#             answer+=1
#     return answer

# 144. 피자 나눠 먹기 (3)
