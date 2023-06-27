# 31. 수 조작하기1
# def solution(n, control):
#     for i in control:
#         if i == "w": n+=1
#         elif i == "s": n-=1
#         elif i == "a": n-=10
#         elif i == "d": n+=10
#         else: continue
#     return n

# def solution(n, control):
#     key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
#     return n + sum([key[c] for c in control])

# 32. 수 조작하기2
# def solution(numLog):
#     strLog = {1:'w', -1:'s', 10:'d', -10:'a'}
#     answer=''
#     for i in range(len(numLog)-1):
#         x = numLog[i+1] - numLog[i]
#         answer += strLog[x]
#     return answer

# 33. 수열과 구간 쿼리 2
# def solution(arr, queries):
#     result=[]
#     for n in range(len(queries)):
#         a = []
#         b = arr[queries[n][0]:queries[n][1]+1]
#         a+=(list(filter(lambda x: x>queries[n][2], b)))
#         if len(a)==0: 
#             result.append(-1)
#         else: 
#             result.append(min(a))
#     return result

# 34. 수열과 구간 쿼리 3
# def solution(arr, queries):
#     for i, j in queries:
#         arr[i], arr[j] = arr[j], arr[i]
#     return arr

# 35. 수열과 구간 쿼리 4
# def solution(arr, queries):
#     for s, e, k in queries:
#         n = list(range(s,e+1))
#         for i in n:
#             if i%k==0:
#                 arr[i]+=1
#     return arr

# 36. n 번째 원소까지
# def solution(num_list, n):
#     return num_list[:n]

# 37. 정수 부분
# def solution(flo):
#     return int(flo)

# 38. rny_string
# def solution(rny_string):
#     return rny_string.replace("m","rn")

# 39. 글자 이어 붙여 문자열 만들기
# def solution(my_string, index_list):
#     answer = ''
#     for i in index_list:
#         answer+=list(my_string)[i]
#     return answer
#     짧게 - return ''.join([my_string[idx] for idx in index_list])

# 40. 두 수의 합
# def solution(a, b):
#     return str(int(a) + int(b))