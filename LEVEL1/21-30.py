# 21. 문자열 내림차순으로 배치하기
def solution(s):
    answer = ''.join(sorted(s)[::-1])
    return answer