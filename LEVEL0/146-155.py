# 146. 배열의 평균값
# def solution(numbers):
#     return sum(numbers) / len(numbers)

# 147. 문자열 계산하기
# def solution(my_string):
#     return eval(my_string)
# eval은 실무에서 절대 쓰면 안된다고 한다.
# 좋은 코드
# return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + ')),  -를 +-로 바꾸고 +로 split해서 음수로 만들어줬다.

# 148. 배열 뒤집기
# def solution(num_list):
#     return num_list[::-1]

# 149. 문자 반복 출력하기
# def solution(my_string, n):
#     answer = ''
#     for i in my_string:
#         answer += i*n
#     return answer

# 150. 아이스 아메리카노
# def solution(money):
#     answer = []
#     answer.append(money//5500)
#     answer.append(money%5500)
#     return answer

# 151. 다음에 올 숫자
# def solution(common):
#     if common[1] - common[0] == common[2] - common[1]:
#         common.append(common[-1] + (common[1] - common[0]))
#     else:
#         common.append(common[-1] * (common[1]//common[0]))
#     return common[-1]

# 152. 치킨 쿠폰
# def solution(chicken):
#     answer = 0
#     while(chicken>=10):
#         answer += chicken//10
#         chicken = chicken//10 + chicken%10
#     return answer
# print(solution(100))

# 153. 옷가게 할인 받기
# def solution(price):
#     discount = 0
#     if price >= 100000 and price <300000:
#         discount = 0.05
#     elif price >= 300000 and price <500000:
#         discount = 0.1
#     elif price >= 500000:
#         discount = 0.2
#     return int(price - (price * discount))

# 154. 문자열 뒤집기
# def solution(my_string):
#     return my_string[::-1]

# 155. 저주의 숫자 3
# def solution(n):
#     answer = 0
#     for i in range(1, n+1):
#         answer+=1
#         while(True):
#             if answer%3 != 0 and '3' not in str(answer):
#                 break    
#             answer+=1
#     return answer
# print(solution(40))