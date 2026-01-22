# 세균 증식
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120910
# 알고리즘: 기초
# 작성자: 김재천
# 작성일: 2026. 01. 22. 09:12:39

def solution(n, t):
    answer = 0
    answer = n*(2**t)
    return answer