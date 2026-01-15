# 각도기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120829
# 알고리즘: 기초
# 작성자: 김재천
# 작성일: 2026. 01. 16. 08:08:16

def solution(angle):
    if angle == 180 :
        answer = 4
    elif angle > 90 :
        answer = 3
    elif angle == 90 :
        answer = 2
    else :
        answer = 1
    return answer
