# 2. a 와 b 출력하기
#a, b = map(int, input().strip().split(' '))
#print("a =", a, "\nb =", b)

# 3. 문자열 반복해서 출력하기
# a, b = input().strip().split(' ')
# b = int(b)

# if len(a) < 1 or len(a) > 10:
#     a = input().split(' ')
# if b < 1 or b > 5:
#     b = input()

# print (a * b)

# 4. 대소문자 바꿔서 출력하기
# str = input()
# result = ""

# for i in str:
#     if i.isupper():
#         result += i.lower()
#     elif i.islower():
#         result +=  i.upper()

# print(result)

# print(input().swapcase()) - 가장 간단한 풀이

# 5. 특수문자 출력하기
#print("!@#$%^&*(\\'\"<>?:;")

# 6. a, b가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요.
# a, b = map(int, input().strip().split(' '))
# print(a, '+', b ,'=', a+b)
# print(f'{a} + {b} = {a+b}')

# 7. 문자열 붙여서 출력하기
# str1, str2 = input().strip().split(' ')
# str3 = str1+str2
# print(str3)

# 8. 문자열 돌리기
# str = input()
# for i in str:
#     print(i)

# 9. 홀짝 구분하기
# a = int(input())
# if a%2:
#     print(f'{a} is odd')
# else:
#     print(f'{a} is even')

# 10. 문자열 겹쳐쓰기
# def solution(my_string, overwrite_string, s):
#     answer = ''
#     answer += my_string[0:s]
#     answer += overwrite_string
#     answer += (my_string[len(overwrite_string)+s:])

#     return answer