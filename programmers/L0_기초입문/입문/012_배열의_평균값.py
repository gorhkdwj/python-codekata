# 배열의 평균값
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120817
# 알고리즘: 기초
# 작성자: 김재천
# 작성일: 2026. 01. 16. 08:44:16

from statistics import mean 

def solution(numbers):
    answer = mean(numbers)
    return answer