# 41. 정사각형으로 만들기
# def solution(arr):
#     row = len(arr)
#     col = len(arr[0])
#     if col > row:
#         for i in range(col-row):
#             arr.append([0 for i in range(col)]) # arr.append([0]*m) for문장 안써도 된다.
#     elif col < row:
#         for i in range(len(arr)):
#             arr[i]+=([0 for i in range(row-col)])
#     return arr

# 42. 카운트 업
# def solution(start, end):
#     return list(range(start,end+1))

# 43. 배열 만들기2
# def solution(l, r):
#     answer = []
#     while(l<=r):
#        for i in list(str(l)):
#           if (i != "5") and (i != "0"):
#              check=0
#              break
#           check=1

#        if check == 1:
#           print(l)
#           answer.append(l)
#        l+=1
#     if(len(answer) == 0):
#        answer.append(-1)
#     return answer
# 다른 사람들 풀이 보면 하나하나 주옥같아 봐보자

# 44. 배열 만들기4
# def solution(arr):
#     stk=[]
#     i=0
#     while (i<len(arr)):
#        if len(stk)==0:
#           stk.append(arr[i])
#           i+=1
#        else:
#           if stk[-1] < arr[i]:
#              stk.append(arr[i])
#              i+=1
#           else:
#              stk.pop()  
#     return stk

# 45. 콜라츠 수열 만들기
# def solution(n):
#     answer = []
#     while (n!=1):
#        answer.append(n)
#        if n%2:
#           n= (3*n)+1
#        else:
#           n = n/2
#     answer.append(1)
#     return answer

# 46. 간단한 논리 연산
# def solution(x1, x2, x3, x4):
#     answer = True
#     x5 = False if x1==False and x2==False else True
#     x6 = False if x3==False and x4==False else True
#     answer = True if x5==True and x6==True else False
#     return answer
#     한 줄로 - return (x1 | x2) & (x3 | x4)

# 47. 배열 만들기 1
# def solution(n, k):
#     temp=k
#     answer = []
#     while (k<=n):
#         answer.append(k)
#         k+=temp
#     return answer
#     한 줄 코드 - return [i for i in range(k,n+1,k)]

# 48. 주사위 게임 1
# def solution(a, b):
#     if a%2 == 1 and b%2 == 1:
#         answer = a*a + b*b
#     elif a%2 == 0 and b%2 == 0:
#         answer = abs(a-b)
#     else:
#         answer = 2 * (a+b)
#     return answer

# 49. 소문자로 바꾸기
# def solution(myString):
#     return myString.lower()

# 50. 접미사 배열
# def solution(my_string):
#     answer = []
#     for i in range(len(my_string)):
#         temp = ''
#         temp += my_string[-i:]
#         answer.append(temp)
#     return sorted(answer)