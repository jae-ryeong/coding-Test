# 176. 모스부호 (1)
# def solution(letter):
#     answer = ''
#     morse = { 
#     '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
#     '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
#     '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
#     '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
#     '-.--':'y','--..':'z'}
#     mos_list = letter.split(" ")
#     for value in mos_list:
#         answer += morse.get(value)
    
#     return answer

# 177. 개미 군단
# def solution(hp):
#     answer = hp // 5
#     hp %= 5
    
#     answer += hp // 3
#     hp %= 3
    
#     answer += hp
    
#     return answer

# 178. 가위 바위 보
# def solution(rsp):
#     answer = ''
#     for i in rsp:
#         if i == "2":
#             answer += "0"
#         elif i == "0":
#             answer += "5"
#         else:
#             answer += "2"
#     return answer

# 속도가 빠르다고 한다.
# def solution(rsp):
#     rsp =rsp.replace('2','s')
#     rsp =rsp.replace('5','p')
#     rsp =rsp.replace('0','r')
#     rsp =rsp.replace('r','5')
#     rsp =rsp.replace('s','0')
#     rsp =rsp.replace('p','2')
#     return rsp

#  dict를 이용한 간결한 풀이
# def solution(rsp):
    # d = {'0':'5','2':'0','5':'2'}
    # return ''.join(d[i] for i in rsp)
# 179. 다항식 더하기
# def solution(polynomial):
#     answer = polynomial.split('+')
#     coe = 0
#     con = 0
    
#     for i in answer:
#         if 'x' in i:
#             temp = i.strip().split('x')
            
#             coe += 1 if temp[0] == '' else int(temp[0])
#         else:
#             con += int(i)
            
#     if coe == 0:
#         return str(con)
#     elif coe == 1:
#         if con == 0:
#             return "x"
#         return 'x + ' + str(con)
    
#     if con == 0:
#         return str(coe) + "x"
#     else:
#         return str(coe) + "x + " + str(con)

# isdigit() 함수 사용, return문이 좀 더 깔끔하다
# def solution(polynomial):
#     xnum = 0
#     const = 0
#     for c in polynomial.split(' + '):
#         if c.isdigit():
#             const+=int(c)
#         else:
#             xnum = xnum+1 if c=='x' else xnum+int(c[:-1])
#     if xnum == 0:
#         return str(const)
#     elif xnum==1:
#         return 'x + '+str(const) if const!=0 else 'x'
#     else:
#         return f'{xnum}x + {const}' if const!=0 else f'{xnum}x'

# 180.
print(solution("x"))