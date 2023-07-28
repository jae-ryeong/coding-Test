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
# 179. 
print(solution("205"))