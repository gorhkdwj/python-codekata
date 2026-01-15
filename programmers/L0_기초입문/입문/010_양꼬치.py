# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 김재천
# 작성일: 2026. 01. 16. 08:43:24

def solution(n, k):
    answer = 0
    x = n * 12000
    if n >= 10 and k >= n//10:
        k = k-(n//10)
    y = k * 2000
    answer = x + y
    return answer