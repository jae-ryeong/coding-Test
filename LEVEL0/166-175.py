# 166. 특정 문자 제거하기
# def solution(my_string, letter):
#     return ''.join([i for i in my_string if not(i in letter)])

# 167. 배열 자르기
# def solution(numbers, num1, num2):
#     return numbers[num1:num2+1]

# 168. 평행
# def solution(dots):
#     case = [[0,1],[2,3],[0,2],[1,3],[0,3],[1,2]]
#     idx1, idx2 = 0, 1

#     for _ in range(3):
#         x1, y1 = abs(dots[case[idx1][0]][0] - dots[case[idx1][1]][0]), abs(dots[case[idx1][0]][1] - dots[case[idx1][1]][1])
#         x2, y2 = abs(dots[case[idx2][0]][0] - dots[case[idx2][1]][0]), abs(dots[case[idx2][0]][1] - dots[case[idx2][1]][1])

#         if x1 / y1 == x2 / y2:
#             return 1

#         idx1+=2
#         idx2+=2
#     return 0
# print(solution([[1,1],[2,2],[3,3],[4,17]]))

# 169. 진료순서 정하기
# def solution(emergency):
#     sorted_emergency = sorted(emergency, reverse=True)
#     dic = {string: i+1 for i, string in enumerate(sorted_emergency)}
#     return [dic.get(i) for i in emergency]

# 170. 외계행성의 나이
# def solution(age):
#     answer = ''
#     age_dic = [chr(i) for i in range(97,107)]
#     for i in list(str(age)):
#         answer += age_dic[int(i)]
#     return answer
# 한 줄 코드 - return ''.join([chr(int(i)+97) for i in str(age)])

# 171. 영어가 싫어요
# def solution(numbers):
#     answer = numbers.replace("one","1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9").replace("zero", "0")
#     return int(answer)
# for문으로 바꾸면
# def solution(numbers):
#     for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
#         numbers = numbers.replace(eng, str(num))
#     return int(numbers)

# 172. 순서쌍의 개수
# def solution(n):
#     answer = 0
#     for i in range(1,n+1):
#         if n%i == 0:
#             answer+=1
#     return answer

# 173. 점의 위치 구하기
# def solution(dot):
#     if dot[0] > 0 and dot[1] > 0:
#         return 1
#     elif dot[0] < 0 and dot[1] > 0:
#         return 2
#     elif dot[0] < 0 and dot[1] < 0:
#         return 3
#     else:
#         return 4
    
# 174. 편지
# def solution(message):
#     return 2 * len(message)

# 175. 배열 회전시키기
# def solution(numbers, direction):
#     answer = []
#     if direction == "right":
#         answer.append(numbers[len(numbers)-1])
#         for i in range(len(numbers)-1):
#             answer.append(numbers[i])
#     elif direction == "left":
#         for i in range(1, len(numbers)):
#             answer.append(numbers[i])
#         answer.append(numbers[0])
#     return answer

# def solution(numbers, direction):
#     return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]