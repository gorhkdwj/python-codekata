# 피자 나눠 먹기 (3)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120816
# 알고리즘: 기초
# 작성자: 김재천
# 작성일: 2026. 01. 22. 10:23:49

# x(판) * slice >= n
# x >= n/slice
# x >= (n//slice)+1

def solution(slice, n):
    answer = 0
    x = 0
    if n%slice == 0:
        x = n//slice
    else:
        x = (n//slice)+1
    answer = x
    return answer